import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

img = cv.imread("Study 1/src//koin.jpg")
cv.imshow('koin',img)

#bgr to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#bgr to hsv 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)


#bgr to l*ab fungsi gambar lab adalah untuk mendeteksi warna yang lebih baik
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

#hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_to_bgr',hsv_bgr)

plt.imshow(rgb)
plt.show()

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()


