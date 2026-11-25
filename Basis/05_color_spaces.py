import cv2
import os

image_path = os.path.join('images', 'bird.png')
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('image',image)
cv2.imshow('image_rgb',image_rgb)
cv2.imshow('image_gray',image_gray)
cv2.imshow('image_hsv',image_hsv)

cv2.waitKey(0)