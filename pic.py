import cv2

img = cv2.imread('m.png',0)
height, width = img.shape
print(height,width)

for i in range (0,150):
    for j in range(0,150):
        if i + j > 100 and i + j < 150 :
            img[i, j] = 0
cv2.imshow('output',img)
cv2.waitKey()
