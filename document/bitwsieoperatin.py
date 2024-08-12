import numpy as np
import cv2

img1 = cv2.imread("aa.jpg")
img2 = np.zeros((250, 500, 3), np.uint8)

img2 = cv2.rectangle(img2,  (100, 0),(400, 50), (255, 255, 255), -1)
# ball = img[200:113, 270:194]
# img[273:333, 100:160] = ball
img2 = cv2.resize(img2, (512, 512))
img1 = cv2.resize(img1, (512, 512))

bitand = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitxor = cv2.bitwise_xor(img1, img2)
bitnot1 = cv2.bitwise_not(img1)
bitnot2 = cv2.bitwise_not(img2)
# dat=cv2.add(img, img1)
#add two image together 
# dat=cv2.addWeighted(img, .2, img1, .8, 0 )

# cv2.imshow("bitOr", bitOr)
# cv2.imshow("bitand", bitand)
# cv2.imshow("bitxor", bitxor)
cv2.imshow("bitnot2", bitnot2)
cv2.imshow("bitnot1", bitnot1)
cv2.waitKey(0)
cv2.destroyAllWindows()