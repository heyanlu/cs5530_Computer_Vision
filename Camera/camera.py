import cv2
import numpy as np

class VideoProcessor:
    def __init__(self):
        self.crop = False
        self.resize = False
        self.blur = False
        self.add_box = False
        self.add_text = False
        self.thresholding = False
        self.new_function = False

    def process_frame(self, frame):
        if self.crop:
            frame = frame[60:300, 100:400]  
        if self.resize:
            frame = cv2.resize(frame, (300, 200))  
        if self.blur:
            frame = cv2.GaussianBlur(frame, (31, 31), 0)  
        if self.add_box:
            cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 3) 
        if self.add_text:
            cv2.putText(frame, "OpenCV Video", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        if self.thresholding:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, frame = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # Apply binary thresholding
        if self.new_function:
            frame = cv2.bitwise_not(frame)
        return frame

def main():
    cap = cv2.VideoCapture(0)  
    processor = VideoProcessor()

    if not cap.isOpened():
        print("Error: Could not open video stream or file.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read video frame.")
            break

        frame = processor.process_frame(frame)

        cv2.imshow("Video Frame", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        elif key == ord("c"):
            processor.crop = not processor.crop
        elif key == ord("r"):
            processor.resize = not processor.resize
        elif key == ord("b"):
            processor.blur = not processor.blur
        elif key == ord("a"):
            processor.add_box = not processor.add_box
        elif key == ord("t"):
            processor.add_text = not processor.add_text
        elif key == ord("g"):
            processor.thresholding = not processor.thresholding
        elif key == ord("n"):
            processor.new_function = not processor.new_function

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
