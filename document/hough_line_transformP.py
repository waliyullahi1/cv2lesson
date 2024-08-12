import numpy as np
import cv2

img = cv2.imread("hh.jpg")
img = cv2.resize(img, (512, 512))

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 20, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200 )
cv2.imshow("imge", edges)
for line in lines:
   rho, theta = line[0]
   print(theta)
   a= np.cos(theta)
   b= np.sin(theta)

   x0 = a*rho
   y0 = b*rho
   # X1 stores the rounded off value of (r * cs(theta) 1000 * sin(theta))
   x1 = int(x0 + 1000 * (-b))
   # y1 stores the rounded off value of (r * cs(theta) 1000 * sin(theta))
   y1 = int(y0 + 1000 * (a))
  # y1 stores the rounded off value of (r * cs(theta) 1000 * sin(theta))
   x2 = int(x0 - 1000 * (-b))
     # y1 stores the rounded off value of (r * cs(theta) 1000 * sin(theta))
   y2 = int(y0 - 1000 * (a))

   cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 1)
   print(y1)

cv2.imshow("imgae", img)
cv2.waitKey(0)
cv2.destroyAllWindows()