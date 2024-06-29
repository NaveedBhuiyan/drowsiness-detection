import cv2

class FaceDetector:
    def __init__(self, cascade_path):
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def detect_faces(self, gray_frame):
        return self.face_cascade.detectMultiScale(
            gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

class EyeDetector:
    def __init__(self, cascade_path):
        self.eye_cascade = cv2.CascadeClassifier(cascade_path)

    def detect_eyes(self, roi_gray):
        return self.eye_cascade.detectMultiScale(roi_gray)
