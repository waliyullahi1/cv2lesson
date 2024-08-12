# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)
# panel = np.zeros([100,700,3], np.uint8)

# print(panel)
# while True:
#    ret, frame = cap.read()  # Unpack the tuple
#    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#    lower_green = np.array([0,0,0])
#    upper_green = np.array([70,255,255])
#    mask = cv2.inRange(hsv, lower_green, upper_green)
#    cv2.imshow("frame", frame)
#    cv2.imshow("mask", mask)
#    cv2.imshow("panel", panel)

#    k = cv2.waitKey(30)
#    if k == 27:
#         break 

# cap.release()
# cv2.destroyAllWindows()

# # import cv2
# # original_image = cv2.imread('i.jpg', cv2.IMREAD_COLOR)
# # gray_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
# # _, mask = cv2.threshold(gray_original, 200, 255, cv2.THRESH_BINARY_INV)
# # result = cv2.bitwise_and(original_image, original_image, mask=mask)
# # cv2.imshow('Result', result)
# # cv2.waitKey(0)

# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread('image.jpg', 1)
# plt.imshow(img, cmap='gray')
# plt.show()
import cv2
import numpy as np

print(cv2.getBuildInformation())

# Initialize the camera
cap = cv2.VideoCapture(0)

# Create a blank panel
panel = np.zeros([100, 700, 3], np.uint8)

# Create a background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()  # Unpack the tuple
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for green (you can adjust these values)
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Create a mask for the green color
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Combine the mask and foreground mask
    result = cv2.bitwise_and(frame, frame, mask=fgmask)

    # Show the frames
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Green Mask", mask)
    cv2.imshow("Foreground Mask", fgmask)
    cv2.imshow("Result", result)

    k = cv2.waitKey(30)
    if k == 27:
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
