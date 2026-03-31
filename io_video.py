import os
import cv2

# Read video
video_path = os.path.join('.','data','monkey.mp4')

video = cv2.VideoCapture(video_path)

# Get Fps of video
fps = video.get(cv2.CAP_PROP_FPS)

delay = int(1000 / fps)

# Visualize video
ret = True
while ret:
    ret, frame =  video.read()
    
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(delay)

video.release()
cv2.destroyAllWindows()