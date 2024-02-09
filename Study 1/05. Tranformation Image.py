import cv2 as cv
import numpy as np

img = cv.imread('Study 1/src//koin.jpg')
cv.imshow('Koin', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
translated = translate(img, 100, 100)

#risizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
fliping = cv.flip(img, 0)

cv.imshow('Flip', fliping)
cv.imshow('Risizing', resized)
cv.imshow('Resized', resized)
cv.imshow('Translated', translated)
cv.imshow('Rotated', rotated)

if cv.waitKey(0) & 0xFF == ord('s'):
    cv.imwrite('koin_copy.png', img)
    cv.destroyAllWindows()