import cv2
import numpy as np

from matplotlib import pyplot as plt



img = cv2.imread("hh.jpg", 0)

canny = cv2.Canny(img, 50, 200 )


tittles = ["orginal", "canny" ]
imgs = [img, canny, ]

for i in range(len(tittles)):
    plt.subplot(1,2, i+1), plt.imshow(imgs[i], "gray")
    plt.title(tittles[i])
    plt.xticks([]), plt.yticks([])


plt.show()
