## Nao opencv functions for nao_2_1.py version 1.0
## change log:


import cv
import sys
import os
from collections import deque
from time import time

gftt_list = list() # initialize good features to track for opencv
fast = 0 # initiliaze face detection state for opencv
time_q = deque([1,1,1,1,1,1,1,1,1,1])
old_time = time()
time_old_track = time()
font = cv.InitFont(cv.CV_FONT_HERSHEY_TRIPLEX, 0.5, 0.5, 0.0, 1)

## Find the *.xml file for face detection.
list_path = sys.path
for i in range (0,len(list_path)):
    if os.path.exists(list_path[i]+"/haarcascade_frontalface_alt2.xml"):
        break
   
cascade_front = cv.Load(list_path[i]+"/haarcascade_frontalface_alt2.xml")

class ResolutionCamera:
    def __init__(self):
        self.low = 0
        self.medium = 1
        self.high = 2
        self.very_high=3
        self.res_160x120 = 0  #kQQVGA
        self.res_320x240 = 1  #kQVGA
        self.res_640x480 = 2  #kVGA
        self.res_1280x960 = 3 #k4VGA
        self.resolutionar = [160,120],[320,240],[640,480],[1280,960]
        self.framerate=30


camera_resolution = ResolutionCamera()

class Region:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

################################################################################
## nao.InitVideo() initialises the cv image and sets the variables on Nao.
## It allows you to give up the resolution. But first execute nao.InitProxy()
################################################################################
def cvInitVideo(cameraProxy, resolution_id):
    global key
    global nameId
    global cv_im

    res = camera_resolution.resolutionar[resolution_id]
    framerate=camera_resolution.framerate
    kALColorSpace=0 #BGR: 11, RGB: 13
    
    try:
        nameId = cameraProxy.subscribe("python_GVM2"+str(random.random()*10), resolution_id, kALColorSpace, framerate) #0, 0, 10
    except NameError:
        print 'ALVideoDevice proxy undefined. Are you running a simulated naoqi?'
        return None
    try:
        cv_im = cv.CreateImageHeader((res[0],
                                      res[1]),
                                     cv.IPL_DEPTH_8U, 1)
    except:
        print "Cannot create image header"
        return None
    
    return nameId
        
#################################################################################
## nao.GetImage() gets the image from Nao. You will fist need to execute
## nao.Initvideo()
#################################################################################
def cvGetImage(cameraProxy):
    global img
    global nameId
    global cv_im
    
    gotimage = False
    count = 0
    
    while not gotimage and count < 10:
        try:
            img =cameraProxy.getImageRemote(nameId)
            #pi=Image.frombuffer("L",(img[0],img[1]),img[6]) # original version leading to warnings about future incompatibilities
            #pi=Image.frombuffer("L",(img[0],img[1]),img[6],"raw", "L", 0, -1) # -1 is upside down orientation, 1 upright orientation
            #pi=Image.fromstring("L",(img[0],img[1]),img[6])
            
            gotimage =True
        except NameError:
            print 'ALVideoDevice proxy undefined. Are you running a simulated naoqi?'
            break
        except:
            count = count + 1
            print "problems with video buffer!! Did you initialize nao.InitVideo() the video first?"
    #cv.SetData(cv_im, pi.tostring()) # conversion using PIL not necessary, pass img[6] directly to cv_im
    #cv.Flip(cv_im,cv_im,0) # not needed when using from string
    #key = cv.WaitKey(10) # only useful after a cv.ShowImage("test",cv_im)
    cv.SetData(cv_im, img[6])
    
    return cv_im

################################################################################
## NOTE!! THIS FUNCTION STILL NEEDS TO BE CLEANED UP
## nao.Detect(frame) looks for a face within the "frame".
## it outputs a opencv image with a box around the face, the centre coordinates in approx. radians
## and whether a face is detected
################################################################################
def Detect(frame, draw = True):
    global face1_x
    global face1_y
    global face1_width
    global face1_center
    global old_face1_x
    global old_face1_y
    global old_face1_width
    global fast
    global windowsz
    global cascade_front

    roiscale = 2
    windowscale = 10
    face1_center = (0,0)
    
    if fast>0:
    
        if fast == 3:
            #The cvrectangle defines the ROI that is used for face detection
            #it depends on the previous location of the face and increases in
            #size if no face is detected
            cvrectangle = [face1_x-(face1_width/(roiscale*2)), 
                           face1_y-(face1_width/(roiscale*2)),
                           face1_width+(face1_width/roiscale),
                           face1_width+(face1_width/roiscale)]
            windowsz = face1_width-(face1_width/windowscale) 
            old_face1_x = face1_x # windowsize should be kept as big as possible
            old_face1_y = face1_y # a larger windowsz means faster detection
            old_face1_width = face1_width
        if fast == 2:
            cvrectangle = [old_face1_x-(old_face1_width/(roiscale)),
                           old_face1_y-(old_face1_width/(roiscale)),
                           old_face1_width+(old_face1_width/(roiscale*0.5)),
                           old_face1_width+(old_face1_width/(roiscale*0.5))]
            windowsz = old_face1_width-(old_face1_width/(windowscale/2))
        if fast == 1:
            cvrectangle = [old_face1_x-(old_face1_width/(roiscale*0.5)),
                           old_face1_y-(old_face1_width/(roiscale*0.5)),
                           old_face1_width+(old_face1_width/(roiscale*0.25)),
                           old_face1_width+(old_face1_width/(roiscale*0.25))]
            windowsz = old_face1_width-(old_face1_width/(windowscale/4))
        
        for i in range (0,2): #Make sure the window under consideration is not
            if cvrectangle[i]<0: #outside the camera region. If so, user edge
                cvrectangle[i] = 0

            if i == 0 and (cvrectangle[i]+cvrectangle[i+2]) > frame.width:
                cvrectangle[i+2]= frame.width - cvrectangle[i]

            if i == 1 and (cvrectangle[i]+cvrectangle[i+2]) > frame.height:
                cvrectangle[i+2]= frame.height - cvrectangle[i]

        if draw == True:
            cv.Rectangle(frame, (cvrectangle[0], cvrectangle[1]),
                    (cvrectangle[0]+cvrectangle[2],
                     cvrectangle[1]+cvrectangle[3]),cv.RGB(0,255,0))

        cv.SetImageROI(frame,(int(cvrectangle[0]),int(cvrectangle[1]),int(cvrectangle[2]),int(cvrectangle[3])))


            
    else:
        windowsz = 20
        cv.ResetImageROI(frame)
    
    
    faces = cv.HaarDetectObjects(frame, cascade_front, cv.CreateMemStorage(0),1.2, 6, 1,(windowsz,windowsz))


    cv.ResetImageROI(frame)
        
    try:
        if fast > 0:
            face1_x = faces[0][0][0]+cvrectangle[0] #These results are from the ROI 
            face1_y = faces[0][0][1]+cvrectangle[1] #instead of from the entire image

        else:
            face1_x = faces[0][0][0]
            face1_y = faces[0][0][1]

        face1_width = faces[0][0][2]
        face1_height = faces[0][0][3]
        face1_center = (face1_x + (face1_width/2),face1_y + (face1_height/2))

        region = Region()
        region.x = face1_x
        region.y = face1_y
        region.width = face1_width
        region.height = face1_height
        
        if draw == True:
            cv.Rectangle(frame, (face1_x, face1_y),
                         (face1_x+face1_width,face1_y+face1_height),
                         cv.RGB(255,255,255))
            cv.Circle(frame, face1_center, 2, cv.RGB(255, 0, 0))
        fast = 3
    except:
        fast = fast-1
        region = Region()

    if fast == 3:
        facedetected = True
    else:
        facedetected = False

    face_loc = list(face1_center)
    convrad = 0.55/(frame.width/2)
    face_loc[0] = (face_loc[0] - (frame.width/2))*convrad
    face_loc[1] = (face_loc[1] - (frame.height/2))*convrad
    
    return frame, face_loc, facedetected, region 
    
################################################################################
## Function Framerate(frame) adds the framerate to the provided
## opencv image "frame"
################################################################################
def Framerate(frame):
    global time_q
    global old_time
    global font
    time_q.append(round(time()-old_time,3))
    time_q.popleft()
    old_time = time()
    avg_time = round(sum(time_q)/float(10),5)
    cv.PutText(frame,
               str(avg_time),
               (15,15),
               font,
               cv.RGB(0,0,255))
    return frame

################################################################################
## Is used to see if Nao's head is moving.
################################################################################
def MovingHead():
    time_mov = time()-start_mov_t
    if time_mov > 2*interpol_time:
        return False
    else:
        return True
    return

###############################################################################
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def FindObject(frame):
    global old_frame
    global gftt_list
    global weights
    global existence
    
    if not MovingHead():
        try:
            mask = FrameMask(old_frame, frame)
        except:
            old_frame = cv.CloneImage(frame)
            gftt_list = list()
            return None, None, False
    else:
        old_frame = cv.CloneImage(frame)
        gftt_list = list()
        return None, None, False

    if mask == None:
        gftt_list = list()
        print "2"
        return None, None, False

    ## Find Good Features to track
    if len(gftt_list) < 300:
        #gftt_list.append((GoodFeaturesToTrack(old_frame, mask),1))
        gftt_new, weights_new, existence_new = GoodFeaturesToTrack(old_frame, mask)
 
        if gftt_new != None:
            gftt_list= gftt_list + gftt_new
            weights = weights + weights_new
            existence = existence + existence_new

    gftt_list_new, weights, existence = OpticalFlow(frame,old_frame,gftt_list, weights, existence)
    weights, existence = UpdatePointWeights(gftt_list_new, gftt_list, weights, existence)

    gftt_list = gftt_list_new

    gftt_list, weights, existence = DropPoints(gftt_list, weights, existence)
    gftt_img = DrawPoints(frame,gftt_list)

    if len(gftt_list)>30:
        loc_obj = list()
        loc_obj = AvgPoint(gftt_list,1)
        cv.Circle(gftt_img,loc_obj,4,255,4,8,0)
        convrad = 0.55/(frame.width/2)
        loc_obj = list(loc_obj)
        loc_obj[0]=(loc_obj[0] - (frame.width/2))*convrad
        loc_obj[1]=(loc_obj[1] - (frame.height/2))*convrad
    else: 
        loc_obj = (None, None)
    cv.ShowImage("Good Features",gftt_img)
    cv.ShowImage("Difference", mask) 
    cv.Copy(frame, old_frame)
    if MovingHead():
        print "Object Location = 0"
        loc_obj[0] = 0
        loc_obj[1] = 0
        gftt_list = list()
        old_frame = 0
    return loc_obj[0], loc_obj[1], True
    
###############################################################################
## Subfunction used by "FindObjects()". Returns a difference image
###############################################################################
def FrameMask(old_frame, frame):

    if MovingHead():
        return None
    mask = cv.CloneImage(old_frame)
    cv.AbsDiff(old_frame, frame, mask)
    cv.Threshold(mask,mask, 15, 255, cv.CV_THRESH_BINARY) 
    
    return mask
###############################################################################
## Subfunction used in "FindObjects()" it is used to find the good features to
## to track. Good Features are features in the image that are corners between
## light and darker areas.
###############################################################################
def GoodFeaturesToTrack(image, mask):
    list_gftt = list()
    weights = list()
    existence = list()
    initpoint = 0
    eig_image = cv.CreateMat(image.height ,image.width, cv.CV_32FC1)
    temp_image = cv.CreateMat(image.height, image.width, cv.CV_32FC1)
    gfttar = cv.GoodFeaturesToTrack(image, eig_image, temp_image, 25, 0.01, 5.0, mask, 3, 0, 0.04) 
    gfttar = cv.FindCornerSubPix(image,
                                 gfttar,
                                 (10,10),
                                 (-1, -1),
                                 (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS,20,0.03))


    for i in range (0,len(gfttar)):
        weights.append(1)
        existence.append(1)

    if len(gfttar) == 0:
        return None, None, None
                         
    return gfttar, weights, existence
###############################################################################
## Subfunction used in "FindObjects()". It plots points gftt_list as circles in
## "image".
###############################################################################
def DrawPoints(image,gftt_list):
    gftt_image = cv.CloneImage(image)

    try:
        for i in range(0,len(gftt_list)):
            cv.Circle(gftt_image,gftt_list[i],2,255,1,8,0)
    except:
        pass
    
    return gftt_image
###############################################################################
## Subfunction used in "FindObjects()". It calculates the new location of
## previous points
###############################################################################
def OpticalFlow(imagenew,imageold,gfttar,weights=0,existence=0):

    
    pyrold = cv.CreateImage((imagenew.width,imagenew.height),
                 cv.IPL_DEPTH_32F,
                 1)
    pyrnew = cv.CreateImage((imagenew.width,imagenew.height),
                 cv.IPL_DEPTH_32F,
                 1)
    (gfttarnew,status,track_error)= cv.CalcOpticalFlowPyrLK(imageold,
                            imagenew,
                            pyrold,
                            pyrnew,
                            gfttar,
                            (10,10),
                            5,
                            (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS,20,0.03),
                            0)


    #UpdatePointWeights(list_gftt_new,list_gftt)
    #DropPoints(gf
    return gfttarnew, weights, existence

def OpticalFlowForOrientation(imagenew,imageold,gfttar,weights=0,existence=0):

    pyrold = cv.CreateImage((imagenew.width,imagenew.height),
                 cv.IPL_DEPTH_32F,
                 1)
    pyrnew = cv.CreateImage((imagenew.width,imagenew.height),
                 cv.IPL_DEPTH_32F,
                 1)
    (gfttarnew,status,track_error)= cv.CalcOpticalFlowPyrLK(imageold,
                            imagenew,
                            pyrold,
                            pyrnew,
                            gfttar,
                            (10,10),
                            5,
                            (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS,20,0.03),
                            0)

    for i in range (0,len(status)):
        if status[i] == 0:
            gfttar.pop(i)
            gfttarnew.pop(i)
            
            
    return gfttarnew, gfttar

def UpdatePointWeights(newpoints, oldpoints, weights, existence):
    #remove points that do not move--------------------
    minmove = 1.5 #minimal movement for the point not to disappear
    #Calculate the vector length of the different points
    difference = DifferencePoints(newpoints, oldpoints)

    #fill the weights lists with appropriate values
    for i in range (len(weights),len(newpoints)):
        weights.append(1)
        existence.append(1)
    #i=0

    for i in range(0,len(newpoints)-1):
        weights[i]=weights[i] + (difference[i]-minmove)
        existence[i] = existence[i] + 1
        if weights[i] > 15:
            weights[i] = 15
        i = i+1
    return (weights, existence)

## is used in UpdatePointWeights
def DifferencePoints(newpoints,oldpoints):
    difference2 = list()
##    if type(newpoints) != list:
##        numpy.asarray(newpoints)
##
##    if type(oldpoints) !=list:
##        numpy.asarray(oldpoints)
    
    for i in range(0,len(oldpoints)-1):
        xcoor = math.sqrt(math.pow(newpoints[i][0]-oldpoints[i][0],2))
        ycoor = math.sqrt(math.pow(newpoints[i][1]-oldpoints[i][1],2))
        diff = math.sqrt(math.pow(xcoor,2)+math.pow(ycoor,2))
        difference2.append(diff)
    return difference2

def DropPoints(points, weights, existence):
    i=0
    if MovingHead():
        print "In movement!!!!"
        return (list(),list(),list())
    while i < len(weights)-1:
        if weights[i] < 0 or existence[i] > 15:
            weights.pop(i)
            points.pop(i)
            existence.pop(i)
        else:
            i = i+1
    return (points,weights, existence)

def AvgPoint(gfttar,meanormedian):
    # 0=median, 1=mean
    if meanormedian == 0:
        x = list()
        y = list()
        for i in range (0, len(gfttar)):
            x.append(gfttar[i][0])
            y.append(gfttar[i][1])
        y.sort()
        x.sort()
        indx = len(x)/2
        indy = len(y)/2
        return (x[indx],y[indy])         
    else:
        x = 0
        y = 0
        for i in range (0, len(gfttar)):
            x = x + gfttar[i][0]
            y = y + gfttar[i][1]
        x = x/len(gfttar)
        y = y/len(gfttar)
        return (x, y)
    
