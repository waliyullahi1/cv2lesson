import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt




img = cv.imread("qq.jpg")
img1 = cv.imread("hh.jpg")



img = cv.resize(img, (512, 512))
img1 = cv.resize(img1, (512, 512))


all = np.hstack((img[:, :256],img1[:, :256]))

#  generate Gaussian pyramid for img
image_copy = img1.copy()
gp_image = [image_copy]
for i in range(6):
    image_copy = cv.pyrDown(image_copy)
    gp_image.append(image_copy)

#  generate Gaussian pyramid for img1
image1_copy = img1.copy()
gp_image1 = [image1_copy]
for i in range(6):
    image1_copy = cv.pyrDown(image1_copy)
    gp_image1.append(image1_copy)


#generate laplacian pyramid for img
img_copy = gp_image[5]
Ip_image=[image_copy]

for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_image[i])
    laplacian = cv.subtract(gp_image[i-1], gaussian_expanded)
    Ip_image.append(laplacian)


#generate laplacian pyramid for img1
img1_copy = gp_image1[5]
Ip_image1=[image_copy]

for i in range(5, 0, -1):
    gaussian_expanded1 = cv.pyrUp(gp_image1 [i])
    laplacian1 = cv.subtract(gp_image[i-1], gaussian_expanded1)
    Ip_image1.append(laplacian1)



# now add left and right halves of imga in each leve

img1_img_pyramid = []
n=0
for img_lap, img_lap1 in zip(Ip_image, Ip_image1):
    n+=1
    cls, rows, ch = img_lap1

cv.imshow("image", img)
cv.imshow("image1", img1)
cv.imshow("image2", all)

cv.waitKey(0)
cv.destroyAllWindows()