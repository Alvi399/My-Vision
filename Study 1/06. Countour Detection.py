import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') #digunakan untuk membuat gambar kosong
img = cv.imread('Study 1/src//koin.jpg')
cv.imshow('Koin', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 0) #parameter threshold1 dan threshold 2 berfungsi untuk menentukan nilai threshold, semakin besar nilai threshold semakin besar nilai threshold
cv.imshow('Canny Edges', canny)

#contour detection
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #parameter 125 dan 255 berfungsi untuk menentukan nilai threshold, semakin besar nilai 125 dan 255 semakin besar nilai threshold
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#draw the contours
drawCountour = cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Countour Draw', drawCountour)

print(f'{len(contours)} contour(s) found!')
for countour in contours:
    print(countour)
    area = cv.contourArea(countour)
    print(area)
    cv.drawContours(img, countour, -1, (0,0,255), 2)


if cv.waitKey(0) & 0xFF == ord('s'):
    cv.imwrite('koin_copy.png', img)
    cv.destroyAllWindows()