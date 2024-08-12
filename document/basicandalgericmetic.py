import numpy as np
import cv2

img = cv2.imread("hh.jpg")
img1 = cv2.imread("qq.jpg")
print(img.size)#return a turple f rows, columns, and channels
print(img.size)# return total number of pixels is accessed
print(img.dtype)#return  image datatype is obtained
b,g,r = cv2.split(img)
img = cv2.merge((b, g, r))
 
# ball = img[200:113, 270:194]
# img[273:333, 100:160] = ball
img = cv2.resize(img, (512, 512))
img1 = cv2.resize(img1, (512, 512))


# dat=cv2.add(img, img1)
#add two image together 
dat=cv2.addWeighted(img, .2, img1, .8, 0 )
cv2.imshow("frame", dat)
cv2.waitKey(0)
cv2.destroyAllWindows()