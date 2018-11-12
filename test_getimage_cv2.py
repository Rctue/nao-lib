# -*- coding: cp1252 -*-
import nao_2_0 as nao
import cv2
import random
import numpy as np

video_subscriber_ID="python_GVM2"

def InitVideo(resolution=2, fps=10, color_space=13, camera_idx=0):
    global video_subscriber_ID

##    Parameter ID Name 	ID Value 	Description
##    AL::kQQQQVGA 	8 	Image of 40*30px
##    AL::kQQQVGA 	7 	Image of 80*60px
##    AL::kQQVGA 	0 	Image of 160*120px
##    AL::kQVGA 	1 	Image of 320*240px
##    AL::kVGA 	        2 	Image of 640*480px
##    AL::k4VGA 	3 	Image of 1280*960px
    resolutionar = [160,120],[320,240],[640,480],[1280,960]
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
##    AL::kYUV422ColorSpace 	9 	2 	2 	Native format, 0xY’Y’VVYYUU equivalent to four unsigned char for two pixels. With Y luma for pixel n, Y’ luma for pixel n+1, and U and V are the average chrominance value of both pixels.
##    AL::kYUVColorSpace 	10 	3 	3 	Buffer contains triplet on the format 0xVVUUYY, equivalent to three unsigned char
##    AL::kRGBColorSpace 	11 	3 	3 	Buffer contains triplet on the format 0xBBGGRR, equivalent to three unsigned char
##    AL::kHSYColorSpace 	12 	3 	3 	Buffer contains triplet on the format 0xYYSSHH, equivalent to three unsigned char
##    AL::kBGRColorSpace 	13 	3 	3 	Buffer contains triplet on the format 0xRRGGBB, equivalent to three unsigned char
##    AL::kYYCbCrColorSpace 	14 	2 	2 	TIFF format, four unsigned characters for two pixels.
##    AL::kH2RGBColorSpace 	15 	3 	3 	H from “HSY to RGB” in fake colors.
##    AL::kHSMixedColorSpace 	16 	3 	3 	HS and (H+S)/2.    

    try:
        nameId = nao.cameraProxy.subscribeCamera(video_subscriber_ID, camera_idx, resolution, color_space, fps) #0, 0, 10
    except NameError:
        print 'ALVideoDevice proxy undefined. Are you running a simulated naoqi?'
        return None
    return nameId

def EndVideo():
    global video_subscriber_ID

    try:
        nao.cameraProxy.releaseImage(video_subscriber_ID)
        nao.cameraProxy.unsubscribe(video_subscriber_ID) 
    except:
        print 'Could not unsubscribe from video capture'
        return None
    return nameId

def GetImage(nameId, max_count=10):
    
    gotimage = False
    count = 0
    cv_im=None
    while not gotimage and count < max_count:
        try:
            nao_image =nao.cameraProxy.getImageRemote(nameId)
            cv_im = (np.reshape(np.frombuffer(nao_image[6], dtype = '%iuint8' % nao_image[2]), (nao_image[1], nao_image[0], nao_image[2])))
            gotimage =True
        except NameError:
            print 'ALVideoDevice proxy undefined. Are you running a simulated naoqi?'
            break
        except:
            count = count + 1
            print "Unable to retrieve image form cameraProxy ", nao.cameraProxy, " and nameId ", nameId
  
    return cv_im
    
nao.InitProxy("192.168.0.115",[0])
#nao.InitPose()
nameId=InitVideo(2,10,0,0)
#nao.Move(1,0,0)

while True:
    im=GetImage(nameId)
    cv2.imshow("frame",im)
    key=cv2.waitKey(1)     
                
    if key==ord('q'):
        break
#nao.Crouch()
EndVideo()
nao.sleep(1)
cv2.destroyAllWindows()
