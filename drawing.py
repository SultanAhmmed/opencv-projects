import os
import cv2

img = cv2.imread(os.path.join('.','data','whiteboard.jpg'))
img = cv2.resize(img, (900, 500))

# line
cv2.line(img, (100,150), (500,300), (255,0,0), 5)

# Rectangle
cv2.rectangle(img, (100,150), (500,300), (0,255,0), 5)
cv2.rectangle(img, (200,250), (600,400), (0,255,0), -1)

# Circle
cv2.circle(img, (300,200), 100, (0,0,255), 5)

# Text
cv2.putText(img, "OpenCV", (100,400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0), 5)
cv2.putText(img, "Drawing", (100, 450), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,255,0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)