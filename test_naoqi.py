#import sys
#sys.path.append("/Users/raymond/pynaoqi-python2.7-2.5.7.1-mac64/lib/python2.7/site-packages")

import naoqi
import time
#from naoqi import ALProxy

#tcp://192.168.68.59:49537
robot_ip="127.0.0.1"
robot_port=57864
proxy_dict = {}


def connect_robot(robot_ip, robot_port, proxy_list):
    global proxy_dict
    
    print("connecting to robot " + "tcp://" + robot_ip + ":" + str(robot_port))

    
    for p in proxy_list:
      if p not in proxy_dict.keys():
        try:
          proxy_dict[p] = naoqi.ALProxy(p,robot_ip,robot_port)
        except RuntimeError,e:
          # catch exception
          print("Error ", e," when creating proxy ",p)
    return proxy_dict
  
def init_pose(time_pos=0.5, speed=0.8):
    """Nao will move to initpose."""
    motion_proxy = proxy_dict["ALMotion"]
    motion_proxy.wakeUp() # turn on motors and go to standby position
    #motion_proxy.goToPosture("Stand", speed) # go to Stand position

def crouch(speed=0.8):
    motion_proxy = proxy_dict["ALMotion"]
    posture_proxy = proxy_dict["ALRobotPosture"]
    
    motion_proxy.stopMove() # stop moving
    time.sleep(0.1)
    posture_proxy.goToPosture("Crouch", speed)   # go to crouch position
    #motion_proxy.stiffnessInterpolation('Body',0, 0.5) # turn off motors
    motion_proxy.rest() # go to rest position (turn off motors)
    

def send_commands(text, x, y, theta):
    # simple exmple to send commands using both TTS and motion at the same time
    tts = proxy_dict["ALTextToSpeech"]
    motion = proxy_dict["ALMotion"]
    motion.wakeUp()
    motion.moveInit()
    moveOp = motion.post.moveTo(x,y,theta) #post makes this call non-blocking -> _async = True
    time.sleep(1)
    t0=time.time()
    tts.post.say(text)
    print(time.time()-t0)

    t0=time.time()
    tts.say(text)
    print(time.time()-t0)
    
    

##    # Wait for both operations to terminate.
##    sayOp.wait()
##    moveOp.wait()

def get_sonar_data(robot="pepper"):
    # Simple example to get sonar data from memory.
    almemory = proxy_dict["ALMemory"]

    if robot == "pepper":
        front_sonar = almemory.getData("Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value")
        back_sonar = almemory.getData("Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value")
        print("Front sonar: " + str(front_sonar))
        print("Back sonar: " + str(back_sonar))
        return front_sonar, back_sonar
    else:  # nao    
        left_sonar = almemory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
        right_sonar = almemory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
        print("Left sonar: " + str(left_sonar))
        print("Right sonar: " + str(right_sonar))
        return left_sonar, right_sonar
# # Create a proxy to ALLandMarkDetection
# markProxy = app.session.service("ALLandMarkDetection")
# # Subscribe to the ALLandMarkDetection extractor
# period = 500
# markProxy.subscribe("Test_Mark", period, 0.0 )
# # Get data from landmark detection (assuming landmark detection has been activated).
# data = almemory.getData("LandmarkDetected")
# print("Landmark detected: " + str(data))

def get_image():
    cameraProxy = proxy_dict["ALVideoDevice"]
    resolution_id = 2    # VGA
    kALColorSpace = 11   # RGB
    framerate = 30
    nameId = cameraProxy.subscribe("test_qi", resolution_id, kALColorSpace, framerate) #0, 0, 10
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
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    proxy_dict = connect_robot(robot_ip, robot_port,["ALMemory", "ALMotion", "ALTextToSpeech", "ALVideoDevice", "ALRobotPosture"])

    init_pose()
    
    ### do interesting stuff here, e.g. move while speaking, get sonar data, get images, etc.
    tts = proxy_dict["ALTextToSpeech"]
    tts.say("Hello, I am Nao.")
    time.sleep(5) # wait 5s
    crouch()
    
    # examples of sending commands, getting sonar data, and getting images
    send_commands("Hello, I am moving forward while speaking.", 1, 0, 0)
    get_sonar_data(robot="nao")
    img = get_image()
    display_image(img)  # requires OpenCV to be installed using pip install opencv-python=

    ### after doing stuff, (say something and) crouch
    tts.say("Phew, I am tired.")
    crouch()




