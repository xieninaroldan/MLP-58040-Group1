import cv2
# path
path = r'cat.jpg'

# Using cv2.imread() method
# Using 0 to read image in grayscale mode
img = cv2.imread (path, cv2. IMREAD_GRAYSCALE)

# Displaying the image
cv2.imshow('cat.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()