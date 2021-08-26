import cv2

#reading image
img = cv2.imread(r"C:\Users\Alexander\OneDrive - The University of Sydney (Students)\usyd robotics club\python_opencv_workshop_usrc-main\python_opencv_workshop_usrc-main\Photos\park.jpg")
cv2.imshow('Original Park', img)

# resizing and rescaling
def rescale_frame(frame,scale=0.5):
    #works for images, video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation =cv2.INTER_AREA)

imgRescaled = rescale_frame(img)
cv2.imshow("Rescaled", imgRescaled)

#convert to greyscale
imgGreyscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey',imgGreyscale)

#blur
imgBlur=cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)
#ksize has to be odd numbers
cv2.imshow('Blur',imgBlur)

#canny
imgCanny=cv2.Canny(img,125,200)
cv2.imshow('Canny',imgCanny)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)

imgRotated= rotate(img,-45)
cv2.imshow('Rotate',imgRotated)

# draw a circle
imgCircle = cv2.circle(img,(int(img.shape[1]/2),int(img.shape[0]/2)),40,(255,0,0),thickness=2)
cv2.imshow('Circle',imgCircle)

cv2.waitKey(0)