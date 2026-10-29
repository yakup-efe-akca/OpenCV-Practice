import os
import cv2

image = cv2.imread(os.path.join('images', 'bird.png'))
resized_image = cv2.resize(image, (600, 900))
cropped_image = image[120:350,100:300]

print(image.shape)
print(resized_image.shape)
print(cropped_image.shape)

cv2.imshow('image', image)
cv2.imshow('resized_image', resized_image)
cv2.imshow('cropped_image', cropped_image)

cv2.waitKey(0)