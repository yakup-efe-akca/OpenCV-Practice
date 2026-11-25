import os
import cv2

image_path = os.path.join('videos', 'car.mp4')
video = cv2.VideoCapture(image_path)

ret = True;
while ret:
    ret, frame = video.read()
    if ret: 
        cv2.imshow('frame',frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()