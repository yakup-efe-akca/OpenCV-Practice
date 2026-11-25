import os
import cv2
import numpy as np

image = cv2.imread(os.path.join('images', 'bird.png'))

image_edge = cv2.Canny(image, 200, 300)
image_edge_d = cv2.dilate(image_edge, np.ones((3,3), dtype=np.int8))
image_edge_e = cv2.erode(image_edge_d, np.ones((3,3), dtype=np.int8))

cv2.imshow('image', image)
cv2.imshow('image_edge', image_edge)
cv2.imshow('image_edge_d', image_edge_d)
cv2.imshow('image_edge_e', image_edge_e)
cv2.waitKey(0)