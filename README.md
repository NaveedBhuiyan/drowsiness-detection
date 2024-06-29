# Drowsiness Detection Project

This project aims to detect drowsiness in real-time using a webcam. It utilizes OpenCV and MediaPipe for facial landmark detection and calculates the Eye Aspect Ratio (EAR) to determine if the eyes are closed for a prolonged period, which indicates drowsiness.

## Features

- Real-time drowsiness detection using webcam feed.
- Uses MediaPipe for accurate facial landmark detection.
- Calculates Eye Aspect Ratio (EAR) to determine drowsiness.
- Alerts the user if drowsiness is detected.

## Requirements

- Python 3.6+
- OpenCV
- MediaPipe
- SciPy
- Imutils

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/NaveedBhuiyan/drowsiness-detection.git
    cd drowsiness-detection
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `main.py` script to start the drowsiness detection:

    ```bash
    python main.py
    ```

2. The script will open a window displaying the webcam feed with detected facial landmarks. If drowsiness is detected, an alert will be shown.

## Project Structure

- `config/`: Contains configuration files.
  - `config.py`: Configuration file with constants like EAR threshold and frame count.
- `src/`: Contains source code.
  - `detectors.py`: Contains `FaceDetector` and `EyeDetector` classes for face and eye detection.
  - `eye_status.py`: Contains `EyeStatus` class for checking drowsiness based on EAR.
- `main.py`: Main script to run the drowsiness detection.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [MediaPipe](https://google.github.io/mediapipe/) for facial landmark detection.
- [OpenCV](https://opencv.org/) for computer vision operations.
- [SciPy](https://www.scipy.org/) for scientific computing.

