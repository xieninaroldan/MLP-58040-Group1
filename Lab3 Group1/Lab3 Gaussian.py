import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('banana.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur = cv.GaussianBlur(img,(5,5),200)
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur_rgb),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()