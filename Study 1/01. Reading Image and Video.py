import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1) # 0 untuk webcam, 1 untuk kamera eksternal

while True:
    ret, frame = cap.read() #fungsi read mengembalikan dua nilai, yaitu ret (return) dan frame
    cv.imshow('frame', frame) #menampilkan frame
    print(ret)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() #menutup kamera
cv.destroyAllWindows() #menutup semua jendela
