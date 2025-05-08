# Hand-Based Volume Control

This Python script allows you to control your computer's volume using hand gestures detected by your webcam. By tracking the distance between your thumb and index finger, the script maps this distance to the system's volume level.

## Prerequisites

Before running the script, ensure you have the following installed:

* **Python 3:** Make sure you have Python 3 installed on your system.
* **OpenCV (cv2):** A library for computer vision tasks. Install it using pip:
    ```bash
    pip install opencv-python
    ```
* **NumPy:** A fundamental package for numerical computation in Python. Install it using pip:
    ```bash
    pip install numpy
    ```
* **pycaw:** A library to control the Windows audio API. Install it using pip:
    ```bash
    pip install pycaw
    ```
* **HandTrackingModule.py:** This is a custom module for hand tracking using MediaPipe. You need to have this file in the same directory as the main script. You can find or create such a module that utilizes the MediaPipe library for hand landmark detection.

## Setup

1.  **Install the necessary libraries** as mentioned in the Prerequisites section.
2.  **Obtain the `HandTrackingModule.py` file.** This module should contain the logic for detecting hands and their landmarks from a video stream.
3.  **Save the provided Python code** as a `.py` file (e.g., `volume_control.py`) in the same directory as `HandTrackingModule.py`.

## How to Run

1.  **Connect your webcam** to your computer.
2.  **Open a terminal or command prompt**, navigate to the directory where you saved the Python script and `HandTrackingModule.py`.
3.  **Run the script** using the command:
    ```bash
    python volume_control.py
    ```

## Usage

1.  Once the script runs, a window will open displaying your webcam feed with hand tracking overlays.
2.  Bring your hand in front of the camera. The script will detect your hand and identify key landmarks, particularly the tips of your thumb and index finger.
3.  **Volume Control:**
    * The distance between your thumb and index finger will be mapped to the system's volume level.
    * Bringing your thumb and index finger closer together will decrease the volume.
    * Moving them further apart will increase the volume.
    * A line will be drawn between the tips of your thumb and index finger, and its length visually represents the current volume level.
    * A volume bar will be displayed on the screen, also indicating the volume level.
    * When the thumb and index finger are very close, a green circle will appear, indicating a low volume state.
4.  **Frames Per Second (FPS):** The script also displays the real-time frames per second of the video feed.
5.  **To close the application**, press the `q` key while the webcam window is active.

## Code Explanation

* **Imports:** Imports necessary libraries like `cv2` for image processing, `numpy` for numerical operations, `time` for calculating FPS, the custom `HandTrackingModule` for hand detection, `math` for calculating distances, and `pycaw` for controlling audio.
* **Camera Setup:** Initializes the webcam (`cv2.VideoCapture(0)`) and sets the desired width and height of the captured frames.
* **Volume Initialization:** Uses the `pycaw` library to access and control the system's audio volume. It retrieves the volume range (min and max).
* **Hand Detector:** Creates an instance of the `HandDetector` class from the `HandTrackingModule`.
* **Main Loop:**
    * Reads frames from the webcam.
    * Detects hands in the frame using `detector.findHands()`.
    * Finds the landmarks (coordinates) of the detected hand using `detector.findPosition()`.
    * If landmarks are detected (specifically for the thumb and index finger):
        * Extracts the coordinates of the thumb tip (landmark 4) and index finger tip (landmark 8).
        * Calculates the midpoint between these two fingers.
        * Draws circles at the finger tips and the midpoint, and a line connecting the finger tips.
        * Calculates the Euclidean distance (`length`) between the thumb and index finger tips.
        * **Volume Mapping:** Maps the hand distance (within a defined range of 10 to 180) to the system's volume range (minVolume to maxVolume) using `np.interp()`. It also maps the distance to visual volume bar parameters (height and percentage).
        * Sets the system's master volume level using `volume.SetMasterVolumeLevel(vol, None)`.
        * If the distance between the fingers is very small, it indicates a mute-like state by drawing a green circle at the midpoint.
    * **Visual Feedback:** Draws a rectangle representing the volume bar and fills it according to the calculated volume percentage. Displays the volume percentage as text.
    * **FPS Calculation:** Calculates and displays the frames per second.
    * **Display:** Shows the processed image with hand tracking and volume indicators.
    * **Exit Condition:** Breaks the loop if the 'q' key is pressed.
* **Cleanup:** Releases the webcam and closes all OpenCV windows.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests with improvements or bug fixes.

## License

[Specify your license here, e.g., MIT License]
