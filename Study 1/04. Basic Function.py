import cv2 
import numpy as np
import os

print("Current Working Directory:", os.getcwd())
img = cv2.imread("Study 1/src//koin.jpg",flags=1)

if img is None:
    print('Failed to load image')
else:
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()