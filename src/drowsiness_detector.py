import cv2
import mediapipe as mp
import time
from config.config import FACE_CASCADE_PATH, EYE_CASCADE_PATH, EYE_AR_THRESH, EYE_AR_CONSEC_FRAMES
from src.detectors import FaceDetector, EyeDetector
from src.eye_status import EyeStatus


class DrowsinessDetector:
    def __init__(self):
        self.face_detector = FaceDetector(FACE_CASCADE_PATH)  # You might remove this if not needed with mediapipe
        self.eye_detector = EyeDetector(EYE_CASCADE_PATH)  # Similarly, remove if not needed with mediapipe
        self.eye_status = EyeStatus()
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1,
                                                    min_detection_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.vs = cv2.VideoCapture(0)

    def get_eye_landmarks(self, face_landmarks, frame_shape):
        landmarks = [(int(landmark.x * frame_shape[1]), int(landmark.y * frame_shape[0])) for landmark in
                     face_landmarks.landmark]
        # Adjust landmark indices based on mediapipe's Face Mesh output
        left_eye = [landmarks[i] for i in [33, 133, 160, 158, 153, 144]]
        right_eye = [landmarks[i] for i in [362, 263, 387, 385, 380, 373]]
        return left_eye, right_eye

    def start(self):
        time.sleep(2.0)
        while True:
            ret, frame = self.vs.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_mesh.process(rgb_frame)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    self.mp_drawing.draw_landmarks(frame, face_landmarks, self.mp_face_mesh.FACEMESH_CONTOURS)

                    left_eye, right_eye = self.get_eye_landmarks(face_landmarks, frame.shape)

                    # Calculate eye aspect ratio for left and right eyes
                    leftEAR = EyeStatus.calculate_polygon_area(left_eye)
                    rightEAR = EyeStatus.calculate_polygon_area(right_eye)

                    # Calculate average eye aspect ratio
                    ear = (leftEAR + rightEAR) / 2.0
                    #print(f'EAR: {ear}')

                    # Check for drowsiness
                    if self.eye_status.is_drowsy(ear):
                        print("SLEEEPING WARNING!!!------------------")
                        cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    # Draw landmarks for visualization
                    for (x, y) in left_eye:
                        cv2.circle(frame, (int(x), int(y)), 2, (255, 255, 0), 5)
                    for (x, y) in right_eye:
                        cv2.circle(frame, (int(x), int(y)), 2, (255, 255, 0), 5)
            # Display frame with annotations
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        self.vs.release()
        cv2.destroyAllWindows()


# Example usage:
if __name__ == "__main__":
    detector = DrowsinessDetector()
    detector.start()
