import nao_nocv_2_1 as nao
import time

def testconnect(IP, PORT):
    ALModuleList = ["ALTextToSpeech", "ALAudioDevice", "ALMotion", "ALMemory", "ALFaceDetection", "ALVideoDevice",
                    "ALLeds", "ALFaceTracker", "ALSpeechRecognition", "ALAudioPlayer", "ALVideoRecorder", "ALSonar",
                    "ALRobotPosture", "ALLandMarkDetection", "ALTracker", "ALSoundDetection",
                    "ALSoundLocalization"]
    proxyDict = {}
    proxyDict = proxyDict.fromkeys(ALModuleList, None)
    proxy = range(1, len(ALModuleList) + 1) #start counting from 1 as 0 has special meaning

    print "Connecting proxies:"
    for i in proxy:
        proxyDict[ALModuleList[i - 1]] = nao.ConnectProxy(ALModuleList[i - 1], IP, PORT)

    print ""
    print "Waiting a while"
    for key in proxyDict:
        print key, " -> ", proxyDict[key]

    nao.sleep(3)

    nao.CloseProxy() # not really necessary only to keep track of proxies


def testsonar(maxcount=10):
    nao.InitSonar()
    count=0
    while count<maxcount:
        [sl,sr]= nao.ReadSonar()
        print sl,sr
        count=count+1
    nao.InitSonar(False)

def testsound(maxcount=10):
    nao.InitSoundDetection()
    print "Detecting sound ... ",
    count=0
    succeeded=False
    while count<maxcount:
        detected, timestamp, soundinfo= nao.DetectSound()
        if detected:
            print timestamp, soundinfo
            succeeded=True
        count=count+1
        time.sleep(0.1)
    nao.InitSoundDetection(False)
    if succeeded:
        print "sound detected."
    else:
        print "no detection."
    return succeeded

def testsoundlocalization(maxcount=10):
    nao.InitSoundLocalization()
    print "Detecting sound location ... ",
    count=0
    succeeded=False
    while count<maxcount:
        detected, timestamp, soundinfo= nao.DetectSoundLocation()
        if detected:
            print timestamp, soundinfo
            succeeded=True
        count=count+1
        time.sleep(0.1)
    nao.InitSoundLocalization(False)
    if succeeded:
        print "sound detected."
    else:
        print "no detection."
    return succeeded

def testcamera(maxcount=10):
    max_resolution=nao.resolution.very_high

    nao.InitLandMark()
    for i in range(max_resolution+1):
        #face detection 
        t=time.time()
        nao.InitVideo(i)
        count=0
        while count<maxcount:
            faceposition, detected = nao.ALFacePosition()
            print faceposition, detected
            count=count+1
        print "Face detection at ", nao.resolution.resolutionar[i], " complete at ", time.time()-t

       

        #Landmark detection
        t=time.time()
        count=0
        while count<maxcount:
            detected, timestamp, markerinfo = nao.DetectLandMark()
            print detected, timestamp, markerinfo
            count=count+1
        print "Landmark detection at ",nao.resolution.resolutionar[i], " complete at ",time.time()-t


def testplayer(filename="mp3/Thriller.mp3"):
    id=nao.Play(filename)
    time.sleep(10)
    print "Pausing.." 
    nao.Pause(id)
    time.sleep(10)
    print "Continuing .."
    nao.Resume(id)
    time.sleep(2)
    print "Stop."
    nao.StopPlay()
    time.sleep(1)
    print "Start from position .."
    nao.playFileFromPosition(filename, 20)
    time.sleep(15)
    print "Stop."
    nao.StopPlay()

def testvideorecorder(file_name = 'test_video'):
    nao.Record(file_name)
    time.sleep(5)
    nao.StopRecord()

def testwalking():
    print "Test basic walking ... ",
    try:
        nao.InitPose()
        nao.Move(1,0,0.2)
        time.sleep(3)
        nao.Move(0,0,0)
        nao.Walk(-0.3, 0, -0.2)
        nao.Crouch()
        succeeded=True
        print "succeeded."
    except:
        succeeded=False
        print "failed."

    return succeeded

def testgestures():
    gestures=nao.GetAvailableGestures()
    nao.InitPose()
    for g in gestures:
        print "gesture ", g, 
        nao.RunMovement(g, post=False)
        print " done."
        time.sleep(3)

    nao.Crouch()
        
def testleds():
    leds=nao.GetAvailableLEDPatterns()
    for l in leds:
        print "LED pattern ", l, 
        nao.RunLED(l)
        time.sleep(3)
        print " done."

def testspeech(maxcount=50):
    wordList=["yes","no","hello", "Nao","goodbye"]
    the_language="English"
    nao.InitSpeech(wordList,the_language)
    count=0
    nao.asr.subscribe("MyModule")
    while count<maxcount:
        #nao.memoryProxy.insertData("WordRecognized",[])

        result=nao.DetectSpeech()
        #print result
        if len(result)>0:
            print result
            nao.asr.unsubscribe("MyModule")
            nao.Say("You said: "+result[0]+".")
            time.sleep(0.2)
            nao.asr.subscribe("MyModule")
        time.sleep(0.2)
        count=count+1
    nao.asr.unsubscribe("MyModule")

    
    
if __name__=="__main__":
#   ip="192.168.0.115"
#    port=9559
#    ip="127.0.0.1"
#    port=50021
    ip="192.168.178.186"
    port=9559
    
    testconnect(ip, port)

    nao.InitProxy(ip,[0],port)
#    result=testwalking()
#    result=testsonar(5)
#    result=testcamera()
#    result=testplayer()
    testvideorecorder()
#    result=testsound(50)
#    result=testsoundlocalization(50)
#    result=testleds()
#    result=testgestures()
#    testspeech()
    
    
