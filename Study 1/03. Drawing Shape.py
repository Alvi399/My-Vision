import cv2 as cv
import numpy as np
import os

os.system('cls')
blank = np.zeros((500, 500, 3), dtype='uint8') #digunakan untuk membuat gambar kosong, dtype='uint8' digunakan untuk mengatur tipe data 'unsigned integer 8-bit'
cv.imshow('Blank', blank)
cv.rectangle(img=blank,pt1=(0,100),pt2=(250,250),color=(0,255,0),thickness=2) #parmeter pt1 dan pt2 digunakan untuk mengatur ukuran kotak
cv.imshow('Rectangle', blank)
cv.waitKey(0) #digunakan untuk menahan gambar yang muncul