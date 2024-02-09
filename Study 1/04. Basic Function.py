import cv2 
import numpy as np
import os
"""
"""
print("Current Working Directory:", os.getcwd())
img = cv2.imread("Study 1/src//koin.jpg",flags=1)
#Using CVtColor to convert the image to grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
#Using gaussian blur to reduce the noise in the image
blur = cv2.GaussianBlur(src=gray, ksize=(7,7), sigmaX=cv2.BORDER_DEFAULT) #parameter ksize berfungsi untuk menentukan ukuran kernel, semakin besar nilai ksize semakin besar ukuran kernel
#parameter sigmaX berfungsi untuk menentukan nilai standard deviation

#Edge cascade - adalah teknik untuk mendeteksi tepi pada gambar, menggunakan teknik ini kita bisa mendeteksi tepi pada gambar
canny = cv2.Canny(image=blur, threshold1=125, threshold2=175) #parameter threshold1 dan threshold2 berfungsi untuk menentukan nilai threshold, semakin besar nilai threshold semakin besar nilai threshold

#dilating the image - adalah teknik untuk memperbesar objek pada gambar
dilated = cv2.dilate(src=canny, kernel=(3,3), iterations=1) #parameter kernel berfungsi untuk menentukan ukuran kernel, semakin besar nilai kernel semakin besar ukuran kernel

#Eroding - adalah teknik untuk memperkecil objek pada gambar
eroded = cv2.erode(src=dilated, kernel=(3,3), iterations=1) #parameter kernel berfungsi untuk menentukan ukuran kernel, semakin besar nilai kernel semakin besar ukuran kernel

#resize - adalah teknik untuk mengubah ukuran gambar
resized = cv2.resize(src=img, dsize=(500,500), interpolation=cv2.INTER_CUBIC) #parameter dsize berfungsi untuk menentukan ukuran gambar yang baru, semakin besar nilai dsize semakin besar ukuran gambar, parameter interpolation berfungsi untuk menentukan metode resize yang digunakan

#crop - adalah teknik untuk memotong gambar
cropped = img[50:200, 200:400] #parameter 50:200 berfungsi untuk menentukan ukuran gambar yang baru, semakin besar nilai 50:200 semakin besar ukuran gambar, parameter 200:400
if img is None:
    print('Failed to load image')
else:
    cv2.imshow('Image', img)
    cv2.imshow('Gray Image', gray)
    cv2.imshow('Blur Image', blur)
    cv2.imshow('Canny Image', canny)
    cv2.imshow('Dilated Image', dilated)
    cv2.imshow('Eroded Image', eroded)
    cv2.imshow('Resized Image', resized)
    cv2.imshow('Cropped Image', cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()