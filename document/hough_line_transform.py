import numpy as np
import cv2

img = cv2.imread("hh.jpg")
img = cv2.resize(img, (512, 512))

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 20, 150, apertureSize=3)

lines = cv2.HoughLinesP(edges, 2, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
  x1, y1, x2, y2 = line[0]
  cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 1)
  

cv2.imshow("imge", edges)
cv2.imshow("imgae", img)
cv2.waitKey(0)
cv2.destroyAllWindows()