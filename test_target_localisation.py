import qi
import time

#tcp://192.168.68.151:9559
#robot_ip="192.168.0.111"
robot_ip="127.0.0.1"
robot_port=9559

def connect_robot(robot_ip, robot_port):
    print("connecting to robot " + "tcp://" + robot_ip + ":" + str(robot_port))
    return qi.Application(url= "tcp://"+robot_ip+":"+str(robot_port))

def detect_face(maxcount=10):
    max_resolution=nao.resolution.very_high

    
    for i in range(max_resolution+1):
        #face detection 
        t=time.time()
        #nao.InitVideo(i)
        count=0
        while count<maxcount:
            faceposition, detected = nao.ALFacePosition()
            print(faceposition, detected)
            count=count+1
        print("Face detection at ", nao.resolution.resolutionar[i], " complete at ", time.time()-t)
        
def DetectLandMark(memory_proxy):
    
    data = memory_proxy.getData("LandmarkDetected")
    
    if data==None:
        data=[] # otherwise the next statement fails ...        
    if len(data)==0:
        detected=False
        timestamp=time()
        markerInfo=[]
    else:
        detected=True
        #timestamp=data[0][0]+1E-6*data[0][1] #this works but only if a landmark is detected
        timestamp=time()
        markerInfo=[]
        for p in data[1]:
            markerInfo.append([p[1][0], #markerID
                               p[0][1], #alpha - x location in camera angle
                               p[0][2], #beta  - y location
                               p[0][3], #sizeX
                               p[0][4], #sizeY
                               p[0][5]  #orientation about vertical w.r. Nao's head
                               ])
    return detected, timestamp, markerInfo



def detect_landmark(session, maxcount=10):
    # inti landmark detection
    memory_proxy = session.service("ALMemory")
    landmark_detection = session.service("ALLandMarkDetection")
    landmark_detection.subscribe("LandmarkDetector", 500, 0.0 ) # period of 500ms, no precision threshold
    
    t=time.time()
    count=0
    while count<maxcount:
        detected, timestamp, markerinfo = DetectLandMark(memory_proxy)
        print(detected, timestamp, markerinfo)
        count=count+1
    print("Landmark detection at complete at ",time.time()-t)
        
if __name__ == "__main__":

    app = connect_robot(robot_ip, robot_port)
    app.start()
    session = app.session
    
    detect_landmark(session, maxcount=10)
    



