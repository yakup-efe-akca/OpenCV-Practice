import os
import cv2

image = cv2.imread(os.path.join('images', 'salt-peper-test.jpeg'))

k_size = 9 ;
image_blur = cv2.blur(image, (k_size,k_size))
image_gaussian_blur = cv2.GaussianBlur(image, (k_size,k_size), 3)
image_median_blur = cv2.medianBlur(image, k_size)

cv2.imshow('image', image)
cv2.imshow('image_blur', image_blur)
cv2.imshow('image_gaussian_blur', image_gaussian_blur)
cv2.imshow('image_median_blur', image_median_blur)
cv2.waitKey(0)