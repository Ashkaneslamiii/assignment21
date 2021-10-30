import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

img1 [:,:] = 255 - img1[:,:]
img2 [:,:] = 255 - img2[:,:]

cv2.imshow('output1', img1)
cv2.imshow('output2',img2)
cv2.waitKey()