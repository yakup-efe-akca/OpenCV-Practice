import cv2
import os

image_path = os.path.join('images', 'bird.png')
image = cv2.imread(image_path)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 80, 255, cv2.THRESH_BINARY)

thresh = cv2.blur(thresh, (10,10))
ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('image',image)
cv2.imshow('image_gray',image_gray)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)