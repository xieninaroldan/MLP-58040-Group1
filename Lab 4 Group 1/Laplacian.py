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
    laplacian = cv.Laplacian(src=gray, ddepth=cv.CV_64F)
    filtered_image = cv.convertScaleAbs(laplacian)

    cv.imshow('Laplacian', filtered_image)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
