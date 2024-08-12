import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt










img = cv.imread('hh.jpg', cv.IMREAD_GRAYSCALE)

#ret, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV )

kernel = np.ones((5,5), np.uint8)
dilation = cv.dilate(img, kernel)
errosion = cv.erode(img, kernel, iterations=1)
opening= cv.morphologyEx(img, cv.MORPH_OPEN, kernel )
closing= cv.morphologyEx(img, cv.MORPH_CLOSE, kernel )
mg= cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel )
th= cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel )
tittles = ["image", "dilution", "errosion", "opening", "closing", "mg", "th" ]
imgs = [img, dilation, errosion, opening,closing,mg,th]

for i in range(len(tittles)):
    plt.subplot(2,4, i+1), plt.imshow(imgs[i], "gray")
    plt.title(tittles[i])
    plt.xticks([]), plt.yticks([])


plt.show()