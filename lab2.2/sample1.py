import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if the frame is read correctly, ret is true
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv.imshow('frame', frame)

    # Check for the 'q' key to quit
    if cv.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()
