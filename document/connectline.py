import numpy as np
import cv2
# using to print all the event in the cv2
# events = [i for  i in dir(cv2) if'EVENT' in i ]
# print(events)

def click_event (event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0, 0, 255), -1)
        print(x,", ",y)
        points.append((x,y))
        # print(points, "points")
        # print(points[-1], "last point")
        # print(points[-2], "second last")
        if len(points) >= 2:
            
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5 )
            cv2.imshow("img", img)
        
      #blue first
    #green second
    #red last
# img = np.zeros((512, 512, 3), np.uint8)

img = cv2.imread('hh.jpg')
cv2.imshow("img", img)
points = []
cv2.setMouseCallback("img", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()