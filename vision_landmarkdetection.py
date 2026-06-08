#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Demonstrates how to use the ALLandMarkDetection module."""

import qi
import time
import sys
import argparse


class LandmarkDetector(object):
    """
    We first instantiate a proxy to the ALLandMarkDetection module
    Note that this module should be loaded on the robot's naoqi.
    The module output its results in ALMemory in a variable
    called "LandmarkDetected".
    We then read this ALMemory value and check whether we get
    interesting things.
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(LandmarkDetector, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Connect the event callback.
        self.subscriber = self.memory.subscriber("LandmarkDetected")
        self.subscriber.signal.connect(self.on_landmark_detected)
        # Get the services ALTextToSpeech and ALLandMarkDetection.
        self.tts = session.service("ALTextToSpeech")
        self.landmark_detection = session.service("ALLandMarkDetection")
        self.landmark_detection.subscribe("LandmarkDetector", 500, 0.0 )
        self.got_landmark = False

    def on_landmark_detected(self, value):
        """
        Callback for event LandmarkDetected.
        """
        if value == []:  # empty value when the landmark disappears
            self.got_landmark = False
        elif not self.got_landmark:  # only speak the first time a landmark appears
            self.got_landmark = True
            print("I saw a landmark! ")
            self.tts.say("I saw a landmark! ")
            # First Field = TimeStamp.
            timeStamp = value[0]
            print("TimeStamp is: " + str(timeStamp))

            # Second Field = array of mark_Info's.
            markInfoArray = value[1]
            for markInfo in markInfoArray:

                # First Field = Shape info.
                markShapeInfo = markInfo[0]

                # Second Field = Extra info (ie, mark ID).
                markExtraInfo = markInfo[1]
                print("mark  ID: %d" % (markExtraInfo[0]))
                print("  alpha %.3f - beta %.3f" % (markShapeInfo[1], markShapeInfo[2]))
                print("  width %.3f - height %.3f" % (markShapeInfo[3], markShapeInfo[4]))

    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print("Starting LandmarkDetector")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Interrupted by user, stopping LandmarkDetector")
            self.landmark_detection.unsubscribe("LandmarkDetector")
            #stop
            sys.exit(0)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--ip", type=str, default="127.0.0.1",
    #                     help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    # parser.add_argument("--port", type=int, default=9559,
    #                     help="Naoqi port number")

    # args = parser.parse_args()
    robot_ip = "192.168.0.112" #args.ip
    robot_port = 9559 #args.port
    
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + robot_ip + ":" + str(robot_port)
        app = qi.Application(["LandmarkDetector", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + robot_ip + "\" on port " + str(robot_port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    landmark_detector = LandmarkDetector(app)
    landmark_detector.run()