import os
import cv2

# Read Image
image_path = os.path.join('.','data','bird_image.jpg')

img = cv2.imread(image_path)

# Write Image
cv2.imwrite(os.path.join('.','data','bird_image_out.jpg'),img)

# Visualize image
cv2.imshow('Image', img)
cv2.waitKey(0)