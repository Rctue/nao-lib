# -*- coding: cp1252 -*-
import nao_nocv_2_1 as nao
import cv2
import random
import numpy as np
import time

video_subscriber_ID="python_GVM2"+str(time.time())
use_simulation = False
resolutionar = [160,120],[320,240],[640,480],[1280,960]

def InitVideo(resolution=2, fps=10, color_space=13, camera_idx=0):
    global video_subscriber_ID, resolutionar

##    Parameter ID Name 	ID Value 	Description
##    AL::kQQQQVGA 	8 	Image of 40*30px
##    AL::kQQQVGA 	7 	Image of 80*60px
##    AL::kQQVGA 	0 	Image of 160*120px
##    AL::kQVGA 	1 	Image of 320*240px
##    AL::kVGA 	        2 	Image of 640*480px
##    AL::k4VGA 	3 	Image of 1280*960px
##    Parameter ID Name 	ID Value 	Number of layers 	Number of channels 	Description
##    AL::kYuvColorSpace 	0 	1 	1 	Buffer only contains the Y (luma component) equivalent to one unsigned char
##    AL::kyUvColorSpace 	1 	1 	1 	Buffer only contains the U (Chrominance component) equivalent to one unsigned char
##    AL::kyuVColorSpace 	2 	1 	1 	Buffer only contains the V (Chrominance component) equivalent to one unsigned char
##    AL::kRgbColorSpace 	3 	1 	1 	Buffer only contains the R (Red component) equivalent to one unsigned char
##    AL::krGbColorSpace 	4 	1 	1 	Buffer only contains the G (Green component) equivalent to one unsigned char
##    AL::krgBColorSpace 	5 	1 	1 	Buffer only contains the B (Blue component) equivalent to one unsigned char
##    AL::kHsyColorSpace 	6 	1 	1 	Buffer only contains the H (Hue component) equivalent to one unsigned char
##    AL::khSyColorSpace 	7 	1 	1 	Buffer only contains the S (Saturation component) equivalent to one unsigned char
##    AL::khsYColorSpace 	8 	1 	1 	Buffer only contains the Y (Brightness component) equivalent to one unsigned char
##    AL::kYUV422ColorSpace 	9 	2 	2 	Native format, 0xY�Y�VVYYUU equivalent to four unsigned char for two pixels. With Y luma for pixel n, Y� luma for pixel n+1, and U and V are the average chrominance value of both pixels.
##    AL::kYUVColorSpace 	10 	3 	3 	Buffer contains triplet on the format 0xVVUUYY, equivalent to three unsigned char
##    AL::kRGBColorSpace 	11 	3 	3 	Buffer contains triplet on the format 0xBBGGRR, equivalent to three unsigned char
##    AL::kHSYColorSpace 	12 	3 	3 	Buffer contains triplet on the format 0xYYSSHH, equivalent to three unsigned char
##    AL::kBGRColorSpace 	13 	3 	3 	Buffer contains triplet on the format 0xRRGGBB, equivalent to three unsigned char
##    AL::kYYCbCrColorSpace 	14 	2 	2 	TIFF format, four unsigned characters for two pixels.
##    AL::kH2RGBColorSpace 	15 	3 	3 	H from �HSY to RGB� in fake colors.
##    AL::kHSMixedColorSpace 	16 	3 	3 	HS and (H+S)/2.    

    try:
        nameId = nao.cameraProxy.subscribeCamera(video_subscriber_ID, camera_idx, resolution, color_space, fps) #0, 0, 10
    except NameError:
        print('ALVideoDevice proxy undefined. Are you running a simulated naoqi?')
        return None
    return nameId

def EndVideo():
    global video_subscriber_ID

    try:
        nao.cameraProxy.releaseImage(video_subscriber_ID)
        nao.cameraProxy.unsubscribe(video_subscriber_ID) 
    except:
        print('Could not unsubscribe from video capture')
        return None
    return nameId

def GetImage(nameId, max_count=3):
    
    gotimage = False
    count = 0
    cv_im = None
    while not gotimage and count < max_count:
        try:
            nao_image =nao.cameraProxy.getImageRemote(nameId)
            cv_im = (np.reshape(np.frombuffer(nao_image[6], dtype = '%iuint8' % nao_image[2]), (nao_image[1], nao_image[0], nao_image[2])))
            gotimage =True
        except NameError:
            print('ALVideoDevice proxy undefined. Are you running a simulated naoqi?')
            break
        except:
            count = count + 1
            print("Unable to retrieve image form cameraProxy ", nao.cameraProxy, " and nameId ", nameId)
  
    return cv_im

# load the required trained XML classifiers
# https://github.com/Itseez/opencv/blob/master/
# data/haarcascades/haarcascade_frontalface_default.xml
# Trained XML classifiers describes some features of some
# object we want to detect a cascade function is trained
# from a lot of positive(faces) and negative(non-faces)
# images.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# https://github.com/Itseez/opencv/blob/master
# /data/haarcascades/haarcascade_eye.xml
# Trained XML file for detecting eyes
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# font
font = cv2.FONT_HERSHEY_SIMPLEX
font_origin = (50, 50)
font_scale = 1
font_color = (255, 0, 0)
font_thickness = 1
 
def face_detect(img):
    global face_cascade, eye_cascade

    # convert to gray scale of each frames
    print(img.shape)
    if img.shape[2]==1:
        gray = img
    elif img.shape[2]==3:
        #print("converting image to gray")
        gray = cv2.cvtColor(img,   cv2.COLOR_BGR2GRAY) # cv2.COLOR_YUV420p2RGB
    else:
        print("unknown picture format")
        return None
    
    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        # To draw a rectangle in a face 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]

        # Detects eyes of different sizes in the input image
        eyes = eye_cascade.detectMultiScale(roi_gray) 

        #To draw a rectangle in eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_gray,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
            
    return faces

    # # Display an image in a window
    # cv2.imshow('img',img)

    # # Wait for Esc key to stop
    # k = cv2.waitKey(30) & 0xff
    # if k == 27:
    #     break

    # # # Close the window
    # # cap.release()

if __name__=="__main__":
    if use_simulation:
        # capture frames from a camera
        cap = cv2.VideoCapture(0) # 0 for windows, 1 for mac
    else:
        nao.InitProxy("192.168.0.102",[0])
        #nao.InitPose()
        nameId=InitVideo(2,10,0,0)
        #nao.Move(1,0,0)
    key = ''
    while True: 
        t0 = time.time()
        if use_simulation:
            # reads frames from a camera
            ret, img = cap.read()
            if ret:
                im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            else:
                im = None
        else:   
            im = GetImage(nameId)
        im_read_time = time.time() - t0
        if not im is None:
            #len(im)>0:
            faces = face_detect(im)
            face_detect_time = time.time() - im_read_time - t0
            image = cv2.putText(im, 'im_read_time = '+str(im_read_time), font_origin, font, 
                   font_scale, font_color, font_thickness, cv2.LINE_AA)
            image = cv2.putText(im, 'face_detect_time = '+str(face_detect_time), (50,70), font, 
                   font_scale, font_color, font_thickness, cv2.LINE_AA)

            cv2.imshow("frame",im)
            key=cv2.waitKey(10)     
                
        if key==ord('q'):
            break

    if use_simulation:
        cap.release()
    else:
        nao.Move(0,0,0)
        nao.Crouch()
        EndVideo()
        nao.sleep(1)


    cv2.destroyAllWindows()
