import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') #digunakan untuk membuat gambar kosong
cv.imshow('Blank', blank)
blank[:] =0, 0, 255 #digunakan untuk mengubah warna gambar
cv.imshow('Green', blank)
cv.waitKey(0) #digunakan untuk menahan gambar yang muncul