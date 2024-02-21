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
    edges = cv.Canny(image=gray,threshold1=100,threshold2=200)

    cv.imshow('Original', frame)
    cv.imshow('Canny', edges)

    # Check for the 'q' key to quit
    if cv.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture and the VideoWriter
cap.release()
cv.destroyAllWindows()
