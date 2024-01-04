#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)  # reduces noise effectively than gaussian and average. Used in many advanced computer vision projects
cv.imshow('Median Blur', median)

# Bilateral
# preserves shape boundary or border
# parameter explanation: 
# sigmaColor : tells how much of neighboring colors influences the center pixel
# sigmaSpace : tells how much far pixel gets affected by the result of current pixel blur
bilateral = cv.bilateralFilter(img, 10, 35, 25) # reduces noise effectively than gaussian, average and median. Used in many advanced computer vision projects
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
