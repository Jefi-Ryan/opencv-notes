#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
# Refer: https://www.geeksforgeeks.org/image-resizing-using-opencv-python
# This method suitable for video, image, live video
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# This method works only with live video
capture = cv.VideoCapture(0)
capture.set(3,width) # 3 refers width
capture.set(4,height) # 4 refers height
'''
# To play a video
Refer: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

while True:
    isTrue, frame = capture.read()
    cv.imshow("video",frame)

    if cv.waitKey(1) == ord("d"):
        break

capture.release()  # release the pointer to the video file
cv.destroyAllWindows() # destroy all frames
'''

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
