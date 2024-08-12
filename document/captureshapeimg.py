import numpy as np
import cv2

img = cv2.imread("shapes.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True )
    cv2.drawContours(img, [approx], 0, (0,0,0), 5)
    x= approx.ravel()[0]
    y= approx.ravel()[1]-10

    if len(approx) == 3:
        cv2.putText(img, "triangle", (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,0,0) )
    elif len(approx) == 4:
       x1, y1, w, h=cv2.boundingRect(approx)
       aspectRation = float(w)/h
       print(aspectRation)
       if aspectRation >= 0.95 and aspectRation <= 1.05 :
           cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,0,0) )
       else:
           cv2.putText(img, "triangle", (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,0,0) )

    elif len(approx) == 5:
       cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,0,0) )
    elif len(approx) == 10:
       cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,0,0) )
    elif len(approx) == 3:
       cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,0,0) )

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()