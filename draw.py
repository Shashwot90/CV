import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# blank[:] = 0,0,255
# cv.imshow('Red', blank)

# blank[200:300, 300:400] = 0,0,255
# cv.imshow('red box', blank)

#reectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2) # cv.filled or -1
cv.imshow('Rectangle', blank)

#circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

#line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)

#text on image
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)