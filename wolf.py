import cv2


img = cv2.imread('4.jpg',0)
img = cv2.resize(img, (600,500))

height, width = img.shape

print(height,width)

for i in range (height):
    for j in range (width):
        if img[i][j] <= 162:
            img[i][j]  = 0

cv2.imshow('output',img)
cv2.waitKey()
            