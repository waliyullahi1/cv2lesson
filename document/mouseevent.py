import numpy as np
import cv2
# using to print all the event in the cv2
# events = [i for  i in dir(cv2) if'EVENT' in i ]
# print(events)

def click_event (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,", ",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ",  " + str(y)
        cv2.putText(img, strxy, (x, y), font, .3, (0, 255,255), 2 )
        cv2.imshow("img", img)
    if event == cv2.EVENT_RBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        blue = img[x,y,0]
        green = img[x,y,1] 
        red = img[x,y,2]
        print(green)
        print(blue)
        print(red)
        strxy = str(blue) + ",  " + str(green)+ ",  " + str(red)
        cv2.putText(img, strxy, (x, y), font, .3, (179, 177,177), 2 )
        cv2.imshow("img", img)
    #blue first
    #green second
    #red last
# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('hh.jpg')
cv2.imshow("img", img)

cv2.setMouseCallback("img", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()