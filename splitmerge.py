import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Red', red)
cv.imshow('Green', green)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merge', merged)

cv.waitKey(0)