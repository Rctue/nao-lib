import nao_nocv_1_3 as nao
import time


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
    count=0
    while count<maxcount:
        detected, timestamp, soundinfo= nao.DetectSound()
        print detected, timestamp, soundinfo
        count=count+1
    nao.InitSoundDetection(False)

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


def testplayer(filename="chopin.mp3"):
    id=nao.Play(filename)
    time.sleep(3)
    print "Pausing.." 
    nao.Pause(id)
    time.sleep(1)
    print "Continueing .."
    nao.Pause(id)
    time.sleep(2)
    print "Stop."
    nao.StopPlay()
    time.sleep(1)
    print "Start from position .."
    nao.playFileFromPosition(filename, 100)
    time.sleep(5)
    print "Stop."
    nao.StopPlay()

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

    

    
if __name__=="__main__":
#ip="192.168.0.115"
#    port=9559
    ip="127.0.0.1"
    port=50021
    
    nao.InitProxy(ip,[0],port)
    result=testwalking()
    result=testsonar(5)
#    result=testsound(5)
    result=testcamera()
    result=testplayer()
    
    
