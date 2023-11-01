import cv2 as cv

img = cv.imread('../Photos/lady.jpg') 
cv.imshow('Person', img)



cv.waitKey(0)