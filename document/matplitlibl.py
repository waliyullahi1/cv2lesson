import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("hh.jpg", -1)
cv2.imshow("imgage", img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img)
# plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()