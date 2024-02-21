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

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    sobelxy = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_image_xy = cv.convertScaleAbs(sobelxy)

    edges = cv.Canny(image=gray, threshold1=100, threshold2=200)

    laplacian = cv.Laplacian(src=gray, ddepth=cv.CV_64F)
    filtered_image = cv.convertScaleAbs(laplacian)

    cv.imshow('Original', frame)
    cv.imshow('Sobel XY', filtered_image_xy)
    cv.imshow('Canny', edges)
    cv.imshow('Laplacian', filtered_image)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
