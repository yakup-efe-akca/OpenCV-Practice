import cv2
import os

image_path = os.path.join('images', 'handwritten.png')
image = cv2.imread(image_path)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, simple_thresh = cv2.threshold(image_gray, 80, 255, cv2.THRESH_BINARY)

adaptive_thresh = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 21, 30)

cv2.imshow('image',image)
cv2.imshow('adaptive_thresh',adaptive_thresh)
cv2.imshow('simple_thresh',simple_thresh )
cv2.waitKey(0)