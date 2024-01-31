# Python code to read image
import cv2

img = cv2.imread("cat.jpg", cv2.IMREAD_COLOR)

# Creating GUI window to display an image on screen
cv2.imshow("cat.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()