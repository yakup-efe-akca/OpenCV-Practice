import os
import cv2
import numpy as np

screen = np.ones((1000,1000,3), dtype=np.uint8) * 255

#line
cv2.line(screen, (100, 150), (300, 450), (0, 255, 0), 3)

#rectangle
cv2.rectangle(screen, (400, 150), (600, 250), (0, 0, 255), -1)

#circle
cv2.circle(screen, (150, 600), 100, (255, 0, 0), 4 )

#text
cv2.putText(screen, 'SHAPES', (250, 125), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 3)


cv2.imshow('Screen', screen)
cv2.waitKey(0)
cv2.destroyAllWindows()