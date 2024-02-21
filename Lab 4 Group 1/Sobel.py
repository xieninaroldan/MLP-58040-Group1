import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Cannot open camera')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('Original', frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    sobelx = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
    filtered_image_x = cv.convertScaleAbs(sobelx)
    sobely = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
    filtered_image_y = cv.convertScaleAbs(sobely)
    sobelxy = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_image_xy = cv.convertScaleAbs(sobelxy)

    cv.imshow('Sobel X', filtered_image_x)
    cv.imshow('Sobel Y', filtered_image_y)
    cv.imshow('Sobel XY', filtered_image_xy)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
