import numpy as np
import cv2

img = cv2.imread("qq.jpg")
img = cv2.resize(img, (512, 512))
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print( str(len(contours))) 
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow('img', img)
cv2.imshow("IMAGE GRAY", imgray)
# dat=
cv2.waitKey(0)
cv2.destroyAllWindows()