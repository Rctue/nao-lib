import naoqi
import time
import random
from collections import deque

__errorlevel__ = 0 # 0=verbose, 1=warning, 2=recovered error, 3=mild error, 4=severe error,5=critical error

def log(s, errorlevel):
    if errorlevel>= __errorlevel__:
        print s

##class CircularBuffer(object):
##    def __init__(self, size):
##        """initialization"""
##        self.index= 0
##        self.size= size
##        self._data = []
##
##    def record(self, value):
##        """append an element"""
##        if len(self._data) == self.size:
##            self._data[self.index]= value
##        else:
##            self._data.append(value)
##        self.index= (self.index + 1) % self.size
##
##    def __getitem__(self, key):
##        """get element by index like a regular array"""
##        return(self._data[key])
##
##    def __repr__(self):
##        """return string representation"""
##        return self._data.__repr__() + ' (' + str(len(self._data))+' items)'
##
##    def get_all(self):
##        """return a list of all the elements"""
##        return(self._data)

class State():
    mystate={}
    buffer_size = 10
    
    def set(self, statename, values):
        if statename not in self.mystate.keys():
            self.mystate[statename]=deque([],self.buffer_size)
        self.mystate[statename].append(values)
        

    def get(self, statename):
        #print self.mystate
        try:
            return self.mystate[statename][-1]

        except:
            return None

    def remove(self, statename):
        try:
            del mystate[statename]
            
        except:
            pass

    def __str__(self):
        s=''
        for x in self.mystate.keys():
            s+= str(x)+ "\t" + str(self.mystate[x])+'\n'
        return s
        

class Nao(naoqi.ALModule):
    """ A simple module that connects to the robot and is able to react
    to events.

    """
    NaoBroker = None
    naoqi=None
    def __init__(self, name='NaoBroker', nao_ip='localhost',nao_port=9559):
        self.name=name #Make sure the name you pass to the constructor of ALModule matches the name of your variable.
        if self.NaoBroker == None:
            self.NaoBroker=naoqi.ALBroker(self.name,"0.0.0.0",0,nao_ip,nao_port)
            print "Broker ", self.NaoBroker, " initialized at ", nao_ip, " ", nao_port
        if self.naoqi==None:
            self.naoqi=naoqi.ALModule.__init__(self, name)
        
        try:
            self.motionProxy = naoqi.ALProxy("ALMotion")
            self.robotConfig = self.motionProxy.getRobotConfig()
            for i in range(len(self.robotConfig[0])):
                log(str( self.robotConfig[0][i]) + ": " + str(self.robotConfig[1][i]),0)
            
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)

        try:
            self.memoryProxy = naoqi.ALProxy("ALMemory")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)

        try:
            self.tts = naoqi.ALProxy("ALTextToSpeech")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)

        try:
            self.faceProxy = naoqi.ALProxy("ALFaceDetection")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.faceProxy = None

        try:
            self.ledProxy = naoqi.ALProxy("ALLeds")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.ledProxy = None

        try:
            self.trackfaceProxy = naoqi.ALProxy("ALFaceTracker")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.trackfaceProxy = None

        try:
            self.speechProxy = naoqi.ALProxy("ALSpeechRecognition")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.speechProxy = None

        try:
            self.audioProxy = naoqi.ALProxy("ALAudioDevice")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.audioProxy = None


        try:
            self.cameraProxy = naoqi.ALProxy("ALVideoDevice")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.cameraProxy = None


        try:
            self.playProxy = naoqi.ALProxy("ALAudioPlayer")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.playProxy = None

        try:
            self.videoProxy = naoqi.ALProxy("ALVisionToolbox")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.videoProxy = None

        try:
            self.sonarProxy = naoqi.ALProxy("ALSonar")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.sonarProxy = None

        try:
            self.sensorsProxy= naoqi.ALProxy("ALSensors")
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.sensorsProxy = None
            
        try:
            self.postureProxy= naoqi.ALProxy("ALRobotPosture")
            self.postureList = self.postureProxy.getPostureList()
            log(str(self.postureList),0)
        except RuntimeError as e:
            log( "Error when creating proxies:",3)
            log( str(e),3)
            self.postureProxy = None

    def shutdown(self):
        """Safely shut down NaoBroker"""
        if self.NaoBroker != None:
            self.NaoBroker.shutdown()
            self.NaoBroker = None

    def __del__(self):
        self.shutdown()
    
        

class Nao_Interface(Nao):

#####################################################
### constructor
    def __init__(self, name='NaoBroker', nao_ip='localhost',nao_port=9559):
        self.nao=Nao.__init__(self, name, nao_ip, nao_port)
        time.sleep(1)
        
        self.InitCamera(1)
        self.InitSonar(True)
        
        self.facetrack_targetold = [0.0,0.0]
        self.facetrack_names  = ["HeadYaw","HeadPitch"]
        self.facetrack_interpol_time = 0.5
        self.facetrack_time_old = 0.0
        self.facetrack_id_pose=None
        self.facetrack_start_mov_t=0.0


        
    def InitSonar(self, flag=True):
        
        if not self.sonarProxy:
            log( "Cannot subscribe to sonarProxy. It does not exist",3)
            return
            #period = 100
        #precision = 0.1
        if flag:
            #sonarProxy.subscribe("test4", period , precision )
            try:
                self.sonarProxy.subscribe("Nao_Interface_Sonar")
            except:
                log( "Cannot subscribe to sonarProxy. Does it exist?",3)
        else:
            try:
                self.sonarProxy.unsubscribe("Nao_Interface_Sonar") 
            except:
                log( "Sonar already unsubscribed",3)

    ################################################################################
    ## nao.InitVideo() initialises the cv image and sets the variables on Nao.
    ## It allows you to give up the resolution. But first execute nao.InitProxy()
    ################################################################################
    def InitCamera(self, resolution=1):

## Parameter ID Name	ID Value	Description
## AL::kQQVGA	0	Image of 160*120px
## AL::kQVGA	1	Image of 320*240px
## AL::kVGA	2	Image of 640*480px
## AL::k4VGA	3	Image of 1280*960px

        resolutionar = [160,120],[320,240],[640,480],[1280, 960]
        framerate=30 #only local, wifi with 320x240 is 11fps
        camera=0
        colorspace=0
#        key=0
#        random.random()*10
        try:
            self.cameraId = self.cameraProxy.subscribeCamera("Nao_Interface_Camera", camera, resolution, colorspace, framerate) #0, 0, 10
        except :
            log( 'Cannot subscribe to cameraProxy. Does it exist?',3)
            self.cameraId=None

    #    try:
    #        self.cv_im = cv.CreateImageHeader((resolutionar[resolution][0],
    #                                      resolutionar[resolution][1]),

    #                                     cv.IPL_DEPTH_8U, 1)
    #    except:
    #        print "Cannot create image header"
    #        return None

#####################################################
### destructor
    def __del__(self):
        self.DelCamera()
        self.InitSonar(False)
        
        
    def DelCamera(self):
        try:
            self.cameraProxy.unsubscribe("Nao_Interface_Camera")
        except:
            pass



#####################################################
### actuators
    ### sound and speech synthesis
    def Say(self, text, POST=True):
        try:
            #volume=GetTTSVolume()        
            #SetTTSVolume(0.99)
            if POST:
                self.tts.post.say(text)
            else:
                self.tts.say(text)
            #SetTTSVolume(volume)
        except RuntimeError:
            log( 'Error in Nao_Interface.Say()',3)

    def PlaySine(self,p1,p2,p3,duration):
        """Allows Nao to play a sinusoidal wave of frequency in Hertz p1, Volume gain 0-100  p2, Stereo Pan set to either {-1,0,+1} p3 , duration in seconds"""
        
        try:
            self.audioProxy.playSine(p1,p2,p3,duration)
        except NameError:
            log( 'ALAudioDevice proxy undefined. Are you running a simulated naoqi?',3)

    def StopPlay(self):
        """ Stop music"""
        self.playProxy.stopAll()



    ######################################################
    # Use this class and it's Play() function to play a wav or mp3 file on Nao.
    # The files should be uploaded via ftp. Go to ftp://username:password@nao's_ip
    # And upload them it's initial directory, which is /home/nao/ .
    # id_music
    ######################################################

    def Play(self, file_name):
        """Plays a audio file on Nao, it runs the file from the /home/nao/ directory"""

        file_name = "/home/nao/"+file_name
        self.id_music=self.playProxy.post.playFile(file_name)


    def Pause(self):
        """Pause music"""
        self.playProxy.post.pause(self.id_music)


    ########################
    #playFileFromPosition
    ##############################
    def playFileFromPosition(self, file_name, position):
        file_name = "/home/nao/"+file_name
        self.id_music=playProxy.post.playFileFromPosition(file_name, position)


# just overhead, might as well call directly, maintained for compatibility
    ##########################
    #Set Volume TTS
    ##################################
    def SetTTSVolume(self, volume):
        self.tts.setVolume(volume)

    ##########################
    #Get Volume TTS
    ##################################
    def GetTTSVolume(self):
        vol=self.tts.getVolume()
        return vol

    ##########################
    #Set Volume Music
    ##################################
    def SetMusicVolume(self, volume):
        self.playProxy.setVolume(self.id_music,volume)

    ##########################
    #Get Volume Music
    ##################################
    def GetMusicVolume(self):
        vol=self.playProxy.getMasterVolume()
        return vol


### leds

    ###############################################################################
    ## EyesLED() can change the color of the leds. The color parameter sets
    ## the color in RGB values.
    ## The standard color is off, [0,0,0]. The interpolation time defines the time
    ## in seconds it will take to fully switch to the new color.
    ###############################################################################

    def EyeLED(self, color=[0,0,0], interpol_time = 0, POST=True):
        sGroup = "FaceLeds"
        try:
            if POST:
                self.ledProxy.post.fadeRGB(sGroup, 256*256*color[0] + 256*color[1] + color[2],interpol_time)
            else:
                self.ledProxy.fadeRGB(sGroup, 256*256*color[0] + 256*color[1] + color[2],interpol_time)            
                    
        except NameError:
            log( 'ALLeds proxy undefined.',3)

### head
    ##################################################################################
    ## Moves nao head yaw and pitch of the provided values yaw_val and pitch_val
    ################################################################################
    def MoveHead(self, yaw_val=0, pitch_val=0, isAbsolute=True, post=True, timeLists= [[1],[1]]):

        angleLists = [[yaw_val], [pitch_val]]

        if post==False:
            self.motionProxy.angleInterpolation(self.facetrack_names, angleLists, timeLists, isAbsolute)
        else:
            self.motionProxy.post.angleInterpolation(self.facetrack_names, angleLists, timeLists, isAbsolute)

    def GetYaw(self, useSensors  = True):
        names  = "HeadYaw"
        HeadYaw = self.motionProxy.getAngles(names, useSensors)
        return HeadYaw

    def GetPitch(self, useSensors  = True):
        names  = "HeadPitch"
        useSensors  = True
        HeadPitch = self.motionProxy.getAngles(names, useSensors)
        return HeadPitch

    def GetYawPitch(self, useSensors  = True):
        HeadYawPitch = self.motionProxy.getAngles(self.facetrack_names, useSensors)
        return HeadYawPitch

    def SetYawPitch(self,yaw,pitch,fraction_maxspeed=0.2):
        self.motionProxy.setAngles(["HeadYaw","HeadPitch"], [yaw, pitch], fraction_maxspeed)
        
    ################################################################################
    ## Initializes the track function it stiffens the joints, gathers the IDPose
    ################################################################################
    def InitTrack(self):
        """Stiffening the head joints"""
        self.StiffenHead(1.0)
        
    ################################################################################
    ## Releasing stiffness of the head joints
    ################################################################################
    def EndTrack(self):
        self.StiffenHead(0.0)

    ################################################################################
    ## If the tracking function is initialised you can let nao follow a point in
    ## the camera stream the boolean "detected" specifies whether the target
    ## was detected. "frametime" is the time between frames.
    ################################################################################   
    def Track(target_loc, detected, speed = 5, min_move = 0.04):
        """
        target_loc =  the location Nao's head should move to in radians
        detected = is the head detected, If False target_loc is not used and speed of movement gradually decreases
        (optional) speed = the speed of the movement
        (optional) min_move = the minimal angle of difference between the target_loc and current location for movements to occur.

        """

        self.facetrack_interpol_time = 1.0/speed

        xtarget = target_loc[0]
        ytarget = target_loc[1]

        try:
            frametime = time.time() - self.facetrack_time_old
            self.facetrack_time_old = time.time()
        except:
            log( "Not able to determine frame rate. Guessing...",1)
            frametime = 0.15

        if detected == False:
            xtarget = xtargetold-self.facetrack_targetold[0]*(frametime)
            ytarget = ytargetold-self.facetrack_targetold[1]*(frametime)

        self.facetrack_targetold = [xtarget, ytarget]

        if ((xtarget > min_move or xtarget < -min_move) or (ytarget > min_move or ytarget < -min_move)):
 
            if self.facetrack_id_pose != None:
                self.motionProxy.stop(self.facetrack_id_pose)
                self.facetrack_id_pose = None

            try:
                self.facetrack_id_pose = self.motionProxy.post.angleInterpolation(self.facetrack_names, [-xtarget/2.5,ytarget/2.5] , self.facetrack_interpol_time, False)
                self.facetrack_start_mov_t = time.time()

            except RuntimeError,e:
                print "Kan hoofd niet draaien"
                

    def MovingHead(self):
        """Is used to see if Nao's head is moving."""
        time_mov = time.time()-self.facetrack_start_mov_t
        if time_mov > 2*self.facetrack_interpol_time:
            return False
        else:
            return True
        return

    def ALTrack(self, switch=1):
        """Turn Aldebaran's head tracking on (switch=1) or off (switch=0). Otherwise return status."""

        if not self.trackfaceProxy:
            if switch==1:
                log("trackfaceProxy does not exist.Continuing without facetracking.",1)
            elif switch==0:
                log("trackfaceProxy does not exist.",1)
            else:
                pass
            return False
        
        if switch == 1:
            self.InitTrack()
            self.trackfaceProxy.startTracker()
        elif switch == 0:
            self.trackfaceProxy.stopTracker()
            #self.EndTrack()
        else:
            pass
        
        return self.trackfaceProxy.isActive()
            


#################################################
### body
#################################################
    def Posture(self, pose, speed=1.0):
        if self.postureProxy:
            if pose in self.postureList:
                self.postureProxy.goToPosture(pose, speed)
                return True
        return False
        
    ##############################################################################
    ## Put's Noa into its Initpose. Only use when standing or in crouch position.
    #############################################################################
    def InitPose(self, time_pos=0.5):
        """Nao will move to initpose."""

        if self.Posture("Stand"):
                return

        log("Trying unsafe posture change.",1)

        # stop moving
        self.motionProxy.setWalkTargetVelocity(0,0,0,1)
        time.sleep(0.1)
        # set stiffness
        self.motionProxy.stiffnessInterpolation('Body',1.0, time_pos)
        time.sleep(0.5)

        
        numJoints = len(self.motionProxy.getJointNames('Body'))

        allAngles = [0.0,0.0,                   # head
            1.39, 0.34, -1.39, -1.04, 0.0, 0.0,             # left arm
            0.0, 0.0, -0.43, 0.69, -0.34, 0.0,                  # left leg
            0.0, 0.0, -0.43, 0.69, -0.34, 0.0,                  # right leg
            1.39, -0.34, 1.39, 1.04, 0.0, 0.0]              # right arm
        #printnumJoints
        if (numJoints == 26):
            angles = allAngles
        elif (numJoints == 22):  # no hands (e.g. simulator)
            angles = allAngles[0:6] + allAngles[8:24]
        else:
            log( "error in Init Pose",3)
            
        try:
            self.motionProxy.post.angleInterpolation('Body', angles, 1.5, True);
        
        except RuntimeError,e:
            log( "An error has been caught",3)
            log(str(e),3)
            
    def Stiffen(self, stiffness = 1.0, int_time=0.5):
        """Make Nao stiffen its joints (Can be True or False)"""
        self.motionProxy.stiffnessInterpolation('Body',stiffness, int_time)

    def StiffenHead(self, stiffness = 1.0, int_time=0.5):
        """Make Nao stiffen its head joints (Can be True or False)"""
        self.motionProxy.stiffnessInterpolation(self.facetrack_names,stiffness, int_time)

    def StiffenUpperBody(self, stiffness = 1.0, int_time=0.5):
        """Make Nao stiffen its upper body joints"""

        names=['HeadPitch','HeadYaw','LElbowRoll','LElbowYaw','LHand','LShoulderPitch','LShoulderRoll','LWristYaw','RElbowRoll','RElbowYaw','RHand','RShoulderPitch','RShoulderRoll','RWristYaw']
        stiffnesses=[stiffness,stiffness,stiffness,stiffness,stiffness,stiffness,stiffness,stiffness,stiffness,stiffness,stiffness,stiffness,stiffness,stiffness]
        self.motionProxy.setStiffnesses(names,stiffnesses, int_time)
##        self.motionProxy.setStiffnesses('HeadPitch',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('HeadYaw',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('LElbowRoll',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('LElbowYaw',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('LHand',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('LShoulderPitch',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('LShoulderRoll',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('LWristYaw',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('RElbowRoll',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('RElbowYaw',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('RHand',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('RShoulderPitch',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('RShoulderRoll',int(stiffness), int_time)
##        self.motionProxy.setStiffnesses('RWristYaw',int(stiffness), int_time)

    ################################################################################
    ## Nao crouches and loosens it's joints.
    ###############################################################################
    def Crouch(self):
        """Make Nao to crouch pose."""
        
        if self.Posture("Crouch"):
            self.motionProxy.stiffnessInterpolation('Body',0, 0.5)
            return

        log("Trying unsafe posture change.",1)
#            # get the robot config
#        robotConfig = self.motionProxy.getRobotConfig()
        
            #for i in range(len(robotConfig[0])):
        #    print robotConfig[0][i], ": ", robotConfig[1][i]

        # "Model Type"   : "naoH25", "naoH21", "naoT14" or "naoT2".
        # "Head Version" : "VERSION_32" or "VERSION_33" or "VERSION_40".
        # "Body Version" : "VERSION_32" or "VERSION_33" or "VERSION_40".
        # "Laser"        : True or False.
        # "Legs"         : True or False.
        # "Arms"         : True or False.
        # "Extended Arms": True or False.
        # "Hands"        : True or False.
        # "Arm Version"  : "VERSION_32" or "VERSION_33" or "VERSION_40".
        # Number of Legs : 0 or 2
        # Number of Arms : 0 or 2
        # Number of Hands: 0 or 2
        if self.robotConfig[1][0]=="naoH25" or self.robotConfig[1][0]=="naoH21":
            pass
        else:
            log( "Wrong robot type: cannot crouch without arms and legs",1)
            return
        if self.robotConfig[1][8]=="VERSION_32":
            allAngles = [0.0,0.0,                   # head
                        1.545, 0.33, -1.57, -0.486, 0.0, 0.0,       # left arm
                    -0.3, 0.057, -0.744, 2.192, -1.122, -0.035,     # left leg
                    -0.3, 0.057, -0.744, 2.192, -1.122, -0.035,         # right leg
                        1.545, -0.33, 1.57, 0.486, 0.0, 0.0]        # right arm
        elif self.robotConfig[1][8]=="VERSION_33":
        #Modified for robot version V33
            allAngles = [0.0,0.0,                   # head
                        1.545, 0.2, -1.56, -0.5, 0.0, 0.0,       # left arm
                    -0.319, 0.037, -0.695, 2.11, -1.189, -0.026,     # left leg
                        -0.319, 0.037, -0.695, 2.11, -1.189, -0.026,         # right leg
                    1.545, -0.2, 1.56, 0.5, 0.0, 0.0]        # right arm
        else:
        #Modified for robot version V4.0
            allAngles = [0.0,0.0,                   # head
                        1.53, 0.15, -1.56, -0.5, 0.0, 0.0,       # left arm
                    -0.30, 0.05, -0.75, 2.11, -1.19, -0.04,     # left leg
                        -0.30, 0.05, -0.75, 2.11, -1.19, -0.04,         # right leg
                    1.53, -0.15, 1.56, 0.5, 0.0, 0.0]        # right arm

        numJoints = len(self.motionProxy.getJointNames('Body'))
        if (numJoints == 26):
            angles = allAngles
        elif (numJoints == 22):  # no hands (e.g. simulator)
            angles = allAngles[0:6] + allAngles[8:24]
        else:
            log( "error in numJoints",3)
                
        try:
            self.motionProxy.angleInterpolation('Body', angles, 1.5, True);

        except RuntimeError,e:
            log( "An error has been caught",3)
            log( str(e), 3)

        self.motionProxy.stiffnessInterpolation('Body',0, 0.5)
        
    ##################################################################################
    ## Allows Nao to move in a certain direction with a certain speed.
    ################################################################################
    def Move(self, dx=0, dtheta=0, dy=0 ,freq=1):
        """"
        dx = forward speed, dtheta = rotational speed,
        dy = sidewards speed, freq = step frequency.
        Allows Nao to move in a certain direction
        with a certain speed.
        """
        
        self.motionProxy.setWalkTargetVelocity(dx, dy, dtheta, freq)
        
    ##################################################################################
    ## Allows Nao to move dx meters forward, dy meters sidways with final orientation of dtheta
    ################################################################################
    def Walk(self, dx=0,dy=0,dtheta=0,post=False):
        
        
        """"
        dx = forward meters, dtheta = final angle,

        dy = sidewards meters
        Allows Nao to move in a certain direction.
        
        """
        if post==False:
            self.motionProxy.walkTo(dx, dy, dtheta)
        else:
            self.motionProxy.post.walkTo(dx, dy, dtheta)

            
######################################################
### sensors
######################################################

### tactile
    def HeadTouch(self):
        head_touch = self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value", 0)
        return head_touch

    ### camera
        
    #################################################################################
    ## nao.GetImage() gets the image from Nao. You will fist need to execute
    ## nao.Initvideo()
    #################################################################################
    def GetImage(self):
        """Retrieve remote image from Nao"""
        gotimage = False
        count = 0
        max_count=3
                                               
        while not gotimage and count < max_count:
            try:
                img =self.cameraProxy.getImageRemote(self.cameraId)
                gotimage =True
            except NameError:
                print 'ALVideoDevice proxy undefined. Are you running a simulated naoqi?'
                break
            except:
                count = count + 1
                print "problems with video buffer!! Did you initialize the video first?"

    #    cv.SetData(self.cv_im, pi.tostring())
    #    cv.Flip(self.cv_im,self.cv_im,0)

        return img


    ### sonar
    def ReadSonar(self):    
        
        SonarLeft = "Device/SubDeviceList/US/Left/Sensor/Value"
        SonarRight = "Device/SubDeviceList/US/Right/Sensor/Value"
        SL=self.memoryProxy.getData(SonarLeft,0) # read sonar left value from memory
        SR=self.memoryProxy.getData(SonarRight ,0) # read sonar right value from memory
        return SL, SR

    ### sound

    

#######################################################
### example derived class
#######################################################

class Nao_Events(Nao_Interface):
    """A simple derived class"""

    def __init__(self, name='NaoBroker', nao_ip='localhost',nao_port=9559):
        Nao_Interface.__init__(self, name, nao_ip, nao_port)
        self.state=State()

    def subscribeToEvent(self, event_name, callback_name):
        """Subscribe to the event <name>"""
        log( "Subscribing to event "+str(event_name), 0)
        self.memoryProxy.subscribeToEvent(event_name, self.name, callback_name)       

    def unsubscribeToEvent(self, event_name):
        """Subscribe to the event <name>"""
        self.memoryProxy.unsubscribeToEvent(event_name, self.name)       

    ### example within class callback for Nao_events
    def onTouched(self, strVarName, value, strMessage):
        """callback when data change"""
        log( "datachanged "+ strVarName + " " + str(value) + " " + strMessage, 0)
        
        if value==1:
            if "FrontTactilTouched" in strVarName:
                self.tts.say("That tickles!")
            if "MiddleTactilTouched" in strVarName:
                self.tts.say("Aaaah!")
            if "RearTactilTouched" in strVarName:
                self.tts.say("Ooooh!")

    def onFaceDetected(self, strVarName, value, strMessage):
        """callback when Face detected"""
        #print "datachanged ", strVarName, " ", value, " ", strMessage
        
        if len(value)>0:
            timestamp = value[0]
            face_info=value[1]
            shape_info=face_info[0][0]
            extra_info=face_info[0][1]
            face_id=shape_info[0]
            alpha=shape_info[1]
            beta=shape_info[2]
            size_x=shape_info[3]
            size_y=shape_info[4]

##            print "Face detected:"
##            print "  alpha %.3f - beta %.3f" % (alpha, beta)
##            print "  width %.3f - height %.3f" % (size_x, size_y)

            self.state.set('FaceDetected',[time.time(), alpha, beta, size_x, size_y]) 

            color = [random.randint(0,255),
                     random.randint(0,255),
                     random.randint(0,255)]
            self.ledProxy.post.fadeRGB("FaceLeds", 256*256*color[0] + 256*color[1] + color[2],0.5)

#######################################################
### Main
#######################################################

if __name__=="__main__":
    
    global nao1                         #Make sure to use a global variable for the module instance.
    #nao1=Nao_Events("nao1","192.168.0.115",9559)   #Make sure the name you pass to the constructor of ALModule matches the name of your variable.
    nao1=Nao_Events("nao1","127.0.0.1",9559)   #Make sure the name you pass to the constructor of ALModule matches the name of your variable.
    nao1.Say("Hello")
    nao1.subscribeToEvent("FaceDetected","onFaceDetected")
    nao1.subscribeToEvent("FrontTactilTouched","onTouched")
    nao1.subscribeToEvent("MiddleTactilTouched","onTouched")
    nao1.subscribeToEvent("RearTactilTouched","onTouched")
    nao1.ALTrack(1)
    nao1.InitPose()
    try:
        while True:
            time.sleep(1)
            faceparam = nao1.state.get('FaceDetected')
            if faceparam != None:
                #print time.time()-faceparam[0]
                if (time.time()-faceparam[0])>5:
                    nao1.SetYawPitch(0.0, 0.0, 0.05)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        nao1.Crouch()
        nao1.ALTrack(0)
        nao1.EndTrack()
        nao1.shutdown()

