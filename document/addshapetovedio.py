import cv2
import numpy as np
import datetime
cap =  cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#resize the image of vedio using set   
cap.set(3,700)#for width
cap.set(4,700)#for hight


print(cap.get(3))
print(cap.get(4))

print(cap.isOpened)
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
     font = cv2.FONT_HERSHEY_SIMPLEX
     date= str(datetime.datetime.now())
     text = "width:"+" " + str(cap.get(3)) +" " +"hight:"+" " + str(cap.get(4))
     frame = cv2.putText(frame, date, (20, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
     cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0XFF == ord('s'):
        break

cap.release()

cv2.destroyAllWindows()