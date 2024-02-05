import cv2 
import numpy as np


img = cv2.imread('src/koin.jpg')

if img is None:
    print('Failed to load image')
else:
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()