import cv2


img = cv2.imread('m.png',0)


height, width = img.shape

print(height,width)

for i in range (8):
    for j in range (8):
        if (i+j) % 2 == 0:
            img[i*int(height/8):i*int(height/8)+int(height/8),j*int(width/8):j*int(width/8)+int(width/8)] = 0
        else:
            img[i*int(height/8):i*int(height/8)+int(height/8),j*int(width/8):j*int(width/8)+int(width/8)] = 255

cv2.imshow('output',img)
cv2.waitKey()