import numpy as np
import cv2 as cv

DEFAULT_VIDEO_PATH = 'C:\\Users\\Owner\\PycharmProjects\\pythonProject\\output.avi'

def capture_video():
    cap = cv.VideoCapture(0)



    if not cap.isOpened():
        print("Cannot open camera")
        return

    # Define the codec and create a VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Adjust parameters as needed

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # if the frame is read correctly, ret is true
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv.imshow('frame', frame)

        # Write the frame to the output video file
        out.write(frame)

        # Check for the 'q' key to quit
        if cv.waitKey(1) == ord('q'):
            break

    # When everything is done, release the capture and the VideoWriter
    cap.release()
    out.release()
    cv.destroyAllWindows()

def play_video(file_path=DEFAULT_VIDEO_PATH):
    cap = cv.VideoCapture(file_path)

    if not cap.isOpened():
        print(f"Cannot open video file: {file_path}")
        return

    while cap.isOpened():
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?), Exiting ...")
            break

        cv.imshow('frame', frame)
        if cv.waitKey(30) & 0xFF == 113:  # Use bitwise AND with 0xFF to get the ASCII value
            break

    cap.release()
    cv.destroyAllWindows()

def open_camera():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return

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
        if cv.waitKey(30) & 0xFF == 113:
            break

    # When everything is done, release the capture
    cap.release()
    cv.destroyAllWindows()

def main():
    print("Choose an option:")
    print("1. Capture a video")
    print("2. Play a video")
    print("3. Open the camera without capturing")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        capture_video()
    elif choice == '2':
        play_video()
    elif choice == '3':
        open_camera()
    else:
        print("Invalid choice. Exiting...")

    # Add this line to wait for 'q' key press before exiting
    cv.waitKey(0)

if __name__ == "__main__":
    main()
