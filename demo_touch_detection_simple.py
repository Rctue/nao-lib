# -*- encoding: UTF-8 -*-

"""Example: Say `My {Body_part} is touched` when receiving a touch event"""

import qi
import argparse
import functools
import sys
import time

def subscribe_to_touch(memory_service):
        touch = memory_service.subscriber("TouchChanged")
        id = touch.signal.connect(functools.partial(onTouchChanged, "TouchChanged"))
        
        subscriber = memory_service.subscriber("FrontTactilTouched")
        subscriber.signal.connect(on_touched)

def on_touched(event):
    # value is 1 when pressed, 0 when released
    if event > 0:
        print("ouch")

def onTouchChanged(strVarName, value):
    """ This will be called each time a touch
    is detected.

    """
    print(strVarName, value)
    for p in value:
        print("you touched " + p[0] + " with value " + str(p[1]))


def connect_robot(robot_ip, robot_port):
    print("connecting to robot " + "tcp://" + robot_ip + ":" + str(robot_port))
    return qi.Application(url= "tcp://"+robot_ip+":"+str(robot_port))

def run(memProxy, touchProxy):
    print("Starting touch detection. Press Ctrl+C to stop.")
    memProxy.insertData("TouchChanged", "None") # initialize the variable to avoid None values that would prevent the event callback from being triggered
    try:
        while True:
            time.sleep(1)
            print(memProxy.getData("TouchChanged")) # this is needed to trigger the event callback
            #memProxy.raiseEvent("TouchChanged", ['Head/Touch/Front', False, []]) # this is needed to trigger the event callback
    except KeyboardInterrupt:
        print("Interrupted by user, stopping touch detection")

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--ip", type=str, default="127.0.0.1",
    #                     help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    # parser.add_argument("--port", type=int, default=9559,
    #                     help="Naoqi port number")

    # args = parser.parse_args()
    args_ip = "192.168.0.111"
    args_port = 9559
    app=connect_robot(args_ip, args_port)
   
    app.start()
    session = app.session
    memProxy = session.service("ALMemory")
    tts = session.service("ALTextToSpeech")
    touchProxy = session.service("ALTouch")
    
    #subscribe_to_touch(memProxy)
    
    
    for status in touchProxy.getStatus():
        if "Touch" in status[0]:
            print(status)
            
    for sensor in touchProxy.getSensorList():
        print(sensor)
        
    run(memProxy,touchProxy)
    #app.run()
        