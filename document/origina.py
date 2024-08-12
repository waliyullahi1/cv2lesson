import cv2
from PIL import Image

# Load your grayscale image (already done in previous steps)
input_path = "hh.jpg"
gray = cv2.cvtColor(cv2.imread(input_path), cv2.COLOR_BGR2GRAY)

# Find contours
contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Process each contour
for contour in contours:
    if len(contour) < 5:  # Skip small contours
        continue
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x, y = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
        if len(approx) == 3:
            cv2.putText(gray, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        elif len(approx) == 4:
            cv2.putText(gray, 'Quadrilateral', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# Display the labeled image
cv2.imshow("Labeled Shapes", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
