# -*- coding: cp1252 -*-
import time
import msvcrt
import nao_nocv_2_0 as nao

nao.InitProxy('127.0.0.1')

# NAO Remote Controller

print " NAO remote controller "
print " w: Init Pose"
print " x: Crouch Pose"
print " i: move forward "
print " j: move left "
print " l: move right"
print " a: Stop the robot"
print " t: say something"
print " r: ringing loop"
print " d: Exit remote control"
print " c: Turn Left on spot"
print " b: Turn Right on spot"


exitwhile=0
frequency=1
dx=0
dy=0
dtheta=0

while (exitwhile==0):

    # Ask for input

    #s = raw_input()
    if msvcrt.kbhit():
        s=msvcrt.getch()
    else:
        s=None
    #print s
    if s=="i":
        dx=1
        dy=0
        dtheta=0

    elif s=="j":
        dtheta=0.09
        dx=0.5
        dy=0
        
    elif s=="l":

        dtheta=-0.09
        dx=0.5
        dy=0
    elif s=="c":
        dtheta=0.1
        dx=0
        dy=0
        
    elif s=="b":

        dtheta=-0.1
        dx=0
        dy=0

    elif s=="a":

        dtheta=0
        dx=0
        dy=0
        

    elif s=="w":
        # init pose
        dtheta=0
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
        time.sleep(0.1)            
        try:
            nao.InitPose()
        
        except RuntimeError,e:
            print "An error has been caught"
            print e
                

    elif s=="x":
        # crouch pose
        dtheta=0
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
        time.sleep(0.1)
        nao.Crouch()
        

    elif s=="d":

        dtheta=0
        dx=0
        dy=0
        exitwhile=1

    elif s=="t":
        
        nao.Say('The phone is ringing')
    elif s=="r":
        dx=0
        dy=0
        nao.Move(dx, dy, dtheta, frequency)
        headtouch=False
        
        
        while headtouch == False:
            nao.PlaySine(2000,50,0,1)
            time.sleep(1)
            headtouch = nao.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value", 0)    
            
            
        
    nao.Move(dx, dy, dtheta, frequency)
    time.sleep(0.1)
##    #motionProxy.walkTo(dx, dy, dtheta)


nao.Crouch()






