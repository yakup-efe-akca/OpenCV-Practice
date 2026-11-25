import os
import cv2

image_path = os.path.join('images', 'bird.png')
img = cv2.imread(image_path)

cv2.imwrite(os.path.join('images', 'bird_out.png'), img)

cv2.imshow('image',img)

cv2.waitKey(0)