#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use loadApplication Method"""

import qi
import argparse
import sys
import time


def main(session):
    """
    This example uses the loadApplication method.
    To Test ALTabletService, you need to run the script ON the robot.
    """
    # Get the service ALTabletService.

    try:
        tabletService = session.service("ALTabletService")
        print("Tablet service version:", tabletService.version())
        print("Robot ip:", rbip=tabletService.robotIp())
        
        print("Test screen on/off")
        tabletService.turnOnScreen(False) # turn off the screen
        time.sleep(1)
        tabletService.turnOnScreen(True) # turn on the screen
        time.sleep(1)
        
        print("Test getting touch events for 30s")
        ### getting touch events from the tablet ###
        ############################################        
        # Don't forget to disconnect the signal at the end
        signalID = 0

        # function called when the signal onTouchDown is triggered
        def callback(x, y):
            print("coordinate are x: ", x, " y: ", y)
            if x > 640:
                # disconnect the signal
                #tabletService.onTouchDown.disconnect(signalID)
                pass
    

        # attach the callback function to onJSEvent signal
        signalID = tabletService.onTouchDown.connect(callback)
    
        time.sleep(30)

        
        # disconnect the signal
        tabletService.onTouchDown.disconnect(signalID)
        
        print("Test loading and showing webview for 30s")
        ### displaying picture/webpage on tablet ###
        ############################################        
        
        # Display the index.html page of a behavior name j-tablet-browser
        # The index.html must be in a folder html in the behavior folder
        # /home/nao/.local/share/PackageManager/apps/j-tablet-browser/html/index.html
        # And after loadApplication("j-tablet-browser") the tablet sees it at: http://192.18.0.1/html/index.html
        tabletService.loadApplication("j-tablet-browser")
        tabletService.showWebview('http://192.18.0.1/html/smileys.html') 
        
        #tabletService.showImage('/home/nao/html/tessa_robot.png')
        #tabletService.showImage("http://198.18.0.1/img/help_charger.png")

        # ## from https://developer.softbankrobotics.com/nao6/naoqi-developer-guide/naoqi-python-sdk/naoqi-python-sdk-documentation/tablet-service#showWebview
        #         # Ensure that the tablet wifi is enable
        # tabletService.enableWifi()

        # # Display a web page on the tablet
        # tabletService.showWebview("http://www.google.com") 
        
        # time.sleep(3)

        # # Display a local web page located in boot-config/html folder
        # # The ip of the robot from the tablet is 198.18.0.1
        # tabletService.showWebview("http://198.18.0.1/apps/boot-config/preloading_dialog.html")
        time.sleep(30)

        # Hide the web view
        tabletService.hideWebview()
        
    except Exception as e:
        print("Error was: ", e)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.113",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)