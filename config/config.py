import cv2

# Constants for eye aspect ratio (EAR) calculation
EYE_AR_THRESH = 400  # Threshold to consider an eye as closed
EYE_AR_CONSEC_FRAMES = 20  # Number of consecutive frames the eye must be below the threshold to trigger alert

# Haar cascade files
FACE_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
EYE_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_eye.xml'