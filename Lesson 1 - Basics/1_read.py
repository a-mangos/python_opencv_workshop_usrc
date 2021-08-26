import cv2
import numpy

#reading images
img = cv2.imread(r"C:\Users\Alexander\OneDrive - The University of Sydney (Students)\usyd robotics club\python_opencv_workshop_usrc-main\python_opencv_workshop_usrc-main\Photos\park.jpg")
cv2.imshow('Park', img)

# reading videos

# capture = cv2.VideoCapture('..\Videos\dog.mp4')
# #VideoCapture(0) = Webcam input

# #capture=cv2.VideoCapture(0)

# while True:
#     isTrue,frame=capture.read()
#     #show frame
#     cv2.imshow('',frame)

#     #if the d key is pressed, kill screen
#     if cv2.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv2.destroyAllWindows()

cv2.waitKey(0)
