import cv2 as cv
import numpy as np
import os

blank = np.zeros((500, 500, 3), dtype='uint8') #digunakan untuk membuat gambar kosong, dtype='uint8' digunakan untuk mengatur tipe data 'unsigned integer 8-bit'
# cv.imshow('Blank', blank)

# 1. Menggambar kotak
cv.rectangle(img=blank,pt1=(0,0),pt2=(250,250),color=(0,255,0),thickness=-1,) #parmeter pt1 dan pt2 digunakan untuk mengatur ukuran kotak
# cv.imshow('Rectangle', blank)

# 2. Menggambar lingkaran
cv.circle(img=blank,center=(blank.shape[0]//2,blank.shape[1]//2),radius=40,color=(255,255,255),thickness=1) #parameter center digunakan untuk mengatur posisi lingkaran, radius digunakan untuk mengatur ukuran lingkaran
# cv.imshow('Circle', blank)

# 3. Menggambar garis
cv.line(img=blank,pt1=(0,0),pt2=(blank.shape[0]//2,blank.shape[1]//2),color=(255,255,255),thickness=3) #parameter pt1 dan pt2 digunakan untuk mengatur ukuran garis
#cv.imshow('Line', blank)

# 4. Menggambar text
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.putText(img=blank,text='Hello',org=(255,255),fontFace=cv.FONT_HERSHEY_COMPLEX,fontScale=1.0,color=(0,255,0),thickness=2) #parameter org digunakan untuk mengatur posisi text
cv.imshow('Text', blank)
print(blank.shape)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
