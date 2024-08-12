import cv2
import numpy as np


def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("trackbar")
cv2.createTrackbar("LH", "trackbar", 0, 255, nothing)
cv2.createTrackbar("LS","trackbar",  0, 255, nothing)
cv2.createTrackbar("LV","trackbar",  0, 255, nothing)
cv2.createTrackbar("UH", "trackbar", 255, 255, nothing)
cv2.createTrackbar("US", "trackbar", 255, 255, nothing)
cv2.createTrackbar("UV", "trackbar", 255, 255, nothing)
while (cap.isOpened()):
    ret, frame = cap.read()
    # frame = cv2.imread("hh.jpg")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h  = cv2.getTrackbarPos("LH", "trackbar")
    l_s  = cv2.getTrackbarPos("LS", "trackbar")
    l_v  = cv2.getTrackbarPos("LV", "trackbar")

    u_h  = cv2.getTrackbarPos("UH", "trackbar")
    u_s  = cv2.getTrackbarPos("US", "trackbar")
    u_v  = cv2.getTrackbarPos("UV", "trackbar")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", res)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release
cv2.destroyAllWindows()