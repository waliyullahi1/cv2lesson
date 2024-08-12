import cv2 as cv
import numpy as np


img = cv.imread('qq.jpg', 0)
img = cv.resize(img, (512, 512))

ret, th1 = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow("img1",img)
cv.imshow("image",th1)
cv.imshow("th2",th2)
cv.imshow("th3",th3)
cv.waitKey(0)
cv.destroyAllWindows()