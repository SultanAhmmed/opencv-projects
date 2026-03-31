import os
import cv2

img = cv2.imread(os.path.join('.','data','bird_image.jpg'))

print(img.shape)

cropped_img = img[120:240,50:100]

cv2.imshow('Image',img)
cv2.imshow('Cropped Image',cropped_img)
cv2.waitKey(0)