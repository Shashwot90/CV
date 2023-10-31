import cv2 as cv

img = cv.imread('Photos/cat.jpg') 
cv.imshow('CAt', img)

#gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur removes some noise
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('BLur', blur)

#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#dilate image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resize)

#crop
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)