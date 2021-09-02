import cv2
import numpy as np

# Functions
def translate(img,x,y):
    transMat =np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])

    return cv2.warpAffine(img,transMat,dimensions)

def rescale_frame(frame,scale=0.5):
    #works for images, video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation =cv2.INTER_AREA)

def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)

#reading image
img = cv2.imread(r"../Photos/park.jpg")
cv2.imshow('Original Park', img)

# resizing and rescaling
imgRescaled = rescale_frame(img)
cv2.imshow("Rescaled", imgRescaled)

#convert to greyscale, then blur, then canny
imgGreyscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur_GreyScale=cv2.GaussianBlur(imgGreyscale,(1,9),cv2.BORDER_DEFAULT)
imgCanny_Blur_GreyScale=cv2.Canny(imgBlur_GreyScale,80,200)
cv2.imshow('Canny',imgCanny_Blur_GreyScale)

#Rotation
imgRotated= rotate(img,-45)
cv2.imshow('Rotate',imgRotated)

# Translation
translated = translate(img,100,100)
cv2.imshow('translated', translated)

# Flipping
flip = cv2.flip(img,1)
cv2.imshow('flip',flip)

# draw a circle
imgCircle = cv2.circle(img,(int(img.shape[1]/2),int(img.shape[0]/2)),40,(255,0,0),thickness=2)
cv2.imshow('Circle',imgCircle)

cv2.waitKey(0)