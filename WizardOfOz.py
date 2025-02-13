import time
from math import pi
import msvcrt
import nao_nocv_2_1 as nao
#import numpy as np

# Set Nao IP Address

IP="192.168.0.115"      # IP address of real nao
#IP="127.0.0.1"


nao.InitProxy(IP) # Initialize motion proxy
   

print " NAO remote controller "
print " arrow up: Init Pose"
print " arrow down: Crouch Pose"
print " w: move forward "
print " a: move left "
print " s: Stop the robot"
print " d: move right"
print " r: Run movement"
print " q: Turn Left on spot"
print " e: Turn Right on spot"
print " z: Slowly Turn Left on spot"
print " c: Slowly Turn Right on spot"
print " arrow left : Turn head to Left"
print " arrow right: Turn head to Right"
print " t: Say typed text"
print " Esc: Exit remote control"



exitwhile=0
frequency=1
dx=0
dy=0
dtheta=0
s='a'
nao.motionProxy.stiffnessInterpolation('Head',int(True), 1)
names = ["HeadPitch","HeadYaw"]
turnspeed = 0.05
turnduration = 0.05
faceTracking = False
        #angleLists  = [[1.0, 0.0], [-0.5, 0.5, 0.0]]
        #timeLists   = [[1.0, 2.0], [ 1.0, 2.0, 3.0]]
isAbsolute  = False

while (exitwhile==0):
    # Ask for input
    if msvcrt.kbhit():
        s=msvcrt.getch()
    else:
        time.sleep(0.001) # wait for 1 ms
        s=None
        continue

    if s=="w":
        dx=1
        dy=0
        dtheta=0
        nao.Move(dx, dy, dtheta, frequency)       
    elif s=="a":
        dtheta=0.1
        dx=0.5
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
    elif s=="d":
        dtheta=-0.1
        dx=0.5
        dy=0
        nao.Move(dx, dy, dtheta, frequency)    
    elif s=="q":
        dtheta=0.4
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
    elif s=="e":
        dtheta=-0.4
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
    elif s=="z":
        dtheta=0.2
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
    elif s=="c":
        dtheta=-0.2
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
    elif s=="s":
        dtheta=0
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
    elif ord(s)==27:
        exitwhile=1
    elif s=='f':
        faceTracking = not faceTracking
        nao.ALTrack(faceTracking)
        print "Face tracking is : ", faceTracking      
    elif s=="o":
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
        nao.PlaySine(1000,50,0,2)
    elif s=="p":
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
        nao.PlaySine(1000,50,0,2)        
    elif s=="t":
        s2=raw_input("Enter text to say: ")
        nao.Say(s2)
    elif s=='r':
        gestures = nao.GetAvailableGestures()
        for g in gestures:
            print g
        s2=raw_input("Enter name of gesture: ")
        nao.RunMovement(s2)
    elif s=="1":
        print "Hello!"
        nao.Say('Hello!')        
    elif s=="2":
        nao.Say("Choose a chair.")
    elif s=="3":
        nao.Say('You can now fill out the survey and return to the start position.')
    elif s=="4":
        nao.Say('Thank you for participating.')
    elif s == '\xe0':
        sub = msvcrt.getch()
        if sub == 'H': # up arrow
            print 'Standing up'
            nao.InitPose()
        elif sub == 'M': # left arrow
            #print 'Turn head left'
            turnangle = [0,turnspeed]
            nao.motionProxy.post.angleInterpolation(names, turnangle , turnduration, isAbsolute)
            time.sleep(turnduration)
        elif sub == 'P': # down arrow
            print 'Crouch'
            nao.Crouch()           
        elif sub == 'K': # right arrrow
            #print 'Turn 90 degree right'
            turnangle = [0,-1.0*turnspeed]
            nao.motionProxy.post.angleInterpolation(names, turnangle , turnduration, isAbsolute)
            time.sleep(turnduration)
    # exit while loop

# turn off robot and quit    
nao.ALTrack(False)
nao.Crouch()

