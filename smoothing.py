import cv2 as cv


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

#averaging
average = cv.blur(img, (3,3))
cv.imshow('Average blur', average)

#Gausian blur
gauss =cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gauss)

#median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

#bilateral blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral blur', bilateral)




cv.waitKey(0)