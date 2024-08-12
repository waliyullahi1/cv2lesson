import numpy as np
import cv2
# using to print all the event in the cv2
# events = [i for  i in dir(cv2) if'EVENT' in i ]
# print(events)

def click_event (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       
        blue = img[x,y,0]
        green = img[x,y,1] 
        red = img[x,y,2]
        mycolorImgae = np.zeros((400, 400, 3), np.uint8) 
        mycolorImgae[:]= [blue, green, red]
        cv2.imshow('color', mycolorImgae)

    #blue first
    #green second
    #red last
# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('hh.jpg')
cv2.imshow("img", img)

cv2.setMouseCallback("img", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()