import cv2
import numpy as np

img = cv2.imread("hh.jpg")
layer = img.copy()
gp = [layer]

# Generate Gaussian Pyramid
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)

# Display the top level of the Gaussian Pyramid
layer = gp[5]
cv2.imshow("upper level Gaussian Pyramid", layer)

# Generate Laplacian Pyramid
for i in range(5, 0, -1):
    gussian_extented = cv2.pyrUp(gp[i])
    
    # Ensure the sizes match before subtraction
    if gussian_extented.shape != gp[i-1].shape:
        gussian_extented = cv2.resize(gussian_extented, (gp[i-1].shape[1], gp[i-1].shape[0]))
    
    laplacian = cv2.subtract(gp[i-1], gussian_extented)
    cv2.imshow(str(i), laplacian)

cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
