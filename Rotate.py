import cv2

img1 = cv2.imread('3.jpg')

dim = (500,700)
img_new = cv2.resize(img1, dim)
img_new = cv2.rotate(img_new, rotateCode=cv2.ROTATE_180)
cv2.imshow('output',img_new)
cv2.waitKey()