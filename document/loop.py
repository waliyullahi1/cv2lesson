import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt




img = cv.imread("threshold.jpg", 0)





img = cv.imread('threshold.jpg')
img = cv.resize(img, (512, 512))

ret, th1 = cv.threshold(img, 200, 255, cv.THRESH_BINARY)
ret, th2 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)
ret, th3 = cv.threshold(img, 200, 255, cv.THRESH_TRUNC)
ret, th4 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO)
ret, th5 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO_INV)

tittles = ["orginal image","BINARY","BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV" ]
imgs = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(imgs[i], "gray")
    plt.title(tittles[i])
    plt.xticks([]), plt.yticks([])


plt.show()







# cv.waitKey(0)
# cv.destroyAllWindows()