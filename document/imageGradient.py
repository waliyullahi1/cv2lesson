import cv2
import numpy as np

from matplotlib import pyplot as plt



img = cv2.imread("qq.jpg", cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lapb= np.uint8(np.absolute(lap))

soblex = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobley = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobleX= np.uint8(np.absolute(soblex))
sobleY= np.uint8(np.absolute(sobley))
canny = cv2.Canny(img, 100, 200 )

soblecombined = cv2.bitwise_or(sobleX, sobleY)

tittles = ["orginal","lapb","sobleY","sobleX", "soblecombined", "canny" ]
imgs = [img, lapb, sobleY, sobleX, soblecombined, canny ]

for i in range(len(tittles)):
    plt.subplot(2,5, i+1), plt.imshow(imgs[i], "gray")
    plt.title(tittles[i])
    plt.xticks([]), plt.yticks([])


plt.show()


