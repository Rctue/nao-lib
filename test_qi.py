import qi
import time

#tcp://192.168.68.151:9559
robot_ip="127.0.0.1"
robot_port=62359

app = None

def connect_robot(robot_ip, robot_port):
    print("connecting to robot " + "tcp://" + robot_ip + ":" + str(robot_port))
    return qi.Application(url= "tcp://"+robot_ip+":"+str(robot_port))

def init_pose(session, time_pos=0.5, speed=0.8):
    """Nao will move to initpose."""
    motion_proxy = session.service("ALMotion")
    motion_proxy.wakeUp() # turn on motors and go to standby position
    #motion_proxy.goToPosture("Stand", speed) # go to Stand position

def crouch(session, speed=0.8):
    motion_proxy = session.service("ALMotion")
    posture_proxy = session.service("ALRobotPosture")
    
    motion_proxy.stopMove() # stop moving
    time.sleep(0.1)
    posture_proxy.goToPosture("Crouch", speed)   # go to crouch position
    #motion_proxy.stiffnessInterpolation('Body',0, 0.5) # turn off motors
    motion_proxy.rest() # go to rest position (turn off motors)
    

def send_commands(session, text, x, y, theta):
    # simple exmple to send commands using both TTS and motion at the same time
    tts = session.service("ALTextToSpeech")
    motion = session.service("ALMotion")
    motion.wakeUp()
    motion.moveInit()
    sayOp = tts.say(text,_async=True)
    moveOp = motion.moveTo(x,y,theta,_async=True)

    # Wait for both operations to terminate.
    sayOp.wait()
    moveOp.wait()

def get_sonar_data(session, robot="pepper"):
    # Simple example to get sonar data from memory.
    almemory = session.service("ALMemory")
    sonar_service = session.service("ALSonar")

    # Subscribe to sonars, this will launch sonars (at hardware level)
    # and start data acquisition.
    sonar_service.subscribe("myApplication")


    if robot == "pepper":
        try:
            front_sonar = almemory.getData("Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value")
            back_sonar = almemory.getData("Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value")
        except RuntimeError:
            print("Cannot find sonar device values")
            return None, None
        print("Front sonar: " + str(front_sonar))
        print("Back sonar: " + str(back_sonar))
        return front_sonar, back_sonar
    else:  # nao    
        left_sonar = almemory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
        right_sonar = almemory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
        print("Left sonar: " + str(left_sonar))
        print("Right sonar: " + str(right_sonar))
        return left_sonar, right_sonar

    # Unsubscribe from sonars, this will stop sonars (at hardware level)
    sonar_service.unsubscribe("myApplication")

# # Create a proxy to ALLandMarkDetection
# markProxy = app.session.service("ALLandMarkDetection")
# # Subscribe to the ALLandMarkDetection extractor
# period = 500
# markProxy.subscribe("Test_Mark", period, 0.0 )
# # Get data from landmark detection (assuming landmark detection has been activated).
# data = almemory.getData("LandmarkDetected")
# print("Landmark detected: " + str(data))

def get_image(session):
    cameraProxy = session.service("ALVideoDevice")
    kResolution = 2    # VGA
    kALColorSpace = 11   # RGB
    framerate = 30
    kCamera = 0
##    Parameter ID      Name 	ID Value 	More details ...
##    AL::kTopCamera 	0 	2D Cameras
##    AL::kBottomCamera 1
##    AL::kDepthCamera 	2 	Reconstructed 3D Sensor
##    AL::kStereoCamera 3 	Stereo Camera
    try:
        #naoqi 2.5
        nameId = cameraProxy.subscribe("test_qi", kResolution, kALColorSpace, framerate) #0, 0, 10
    except AttributeError:
        #naoqi 2.8
        nameId = cameraProxy.subscribeCamera("test_qi", kCamera, kResolution, kALColorSpace, framerate)
        
    img =cameraProxy.getImageRemote(nameId)
    print("Image width: " + str(img[0]))
    print("Image height: " + str(img[1]))
    print("Image array size: " + str(len(img[6])))
    cameraProxy.unsubscribe(nameId)
    return img

def display_image(img):
    import cv2
    import numpy as np
    image_width = img[0]
    image_height = img[1]
    array = img[6]
    # Create a numpy array from the image data
    image_array = np.frombuffer(array, dtype=np.uint8)
    # Reshape the array to the correct dimensions (height, width, channels)
    image_array = image_array.reshape((image_height, image_width, 3))
    # Display the image using OpenCV
    cv2.imshow("Captured Image", image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":

    app = connect_robot(robot_ip, robot_port)
    app.start()
    session = app.session
    
    #define proxies:
    memory_proxy = session.service("ALMemory")
    tts_proxy = session.service("ALTextToSpeech")
    video_proxy = session.service("ALVideoDevice")
    
      
    
    init_pose(session)
    
    ### do interesting stuff here, e.g. move while speaking, get sonar data, get images, etc.
    tts_proxy.say("Hello, I am Nao.")
    time.sleep(5) # wait 5s
    crouch(session)
    
    # examples of sending commands, getting sonar data, and getting images
    send_commands(session,"Hello, I am moving forward while speaking.", 1, 0, 0)
    get_sonar_data(session, robot="nao")
    img = get_image(session)
    display_image(img)  # requires OpenCV to be installed using pip install opencv-python=

    ### after doing stuff, (say something and) crouch
    tts_proxy.say("Phew, I am tired.")
    crouch(session)
    app.stop()
