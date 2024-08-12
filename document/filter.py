import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('filter.png')

#ret, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV )



# Create a blur kernel (e.g., 5x5)
kernel = np.ones((5, 5), np.float32) / 25

# Apply the filter2D() function
blurred_image = cv.filter2D(img, -1, kernel)
# Apply the fblur() function
blur = cv.blur(img, (8,8))
gblur = cv.GaussianBlur(img, (5,5), 0)
median = cv.medianBlur(img, 5)
bilateralfilter = cv.bilateralFilter(img, 9, 75, 75)

tittles = ["image","blurred_image", "blur", "gblur", "median ", "bilateralfilter"]
imgs = [img, blurred_image, blur, gblur , median, bilateralfilter]

for i in range(len(tittles)):
    plt.subplot(2,4, i+1), plt.imshow(imgs[i], "gray")
    plt.title(tittles[i])
    plt.xticks([]), plt.yticks([])


plt.show()