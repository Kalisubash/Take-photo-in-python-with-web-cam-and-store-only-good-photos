Webcam Face Capture
This Python script captures images from a webcam, saving only those where faces are detected. It uses OpenCV's Haar Cascade model for real-time face detection.

Features
Real-time Face Detection: Utilizes Haar Cascade to detect faces in webcam feed.
Photo Capture: Saves images when faces are detected, with a maximum of 20 images.
Annotations: Draws rectangles around detected faces for visual feedback.
User Control: Option to stop capturing early by pressing 'q'.

Requirements
Python 3.x
OpenCV library
You can install the required library using pip: pip install opencv-python
You need to install face recognition library to check the quality of photo: pip install face_recognition opencv-python
Usage
Set Up: Ensure your webcam is connected and working.
Directory: Update the output_dir variable in the script to specify where photos will be saved.
Run the Script: Execute the script to start capturing images.

takephoto.py
Capture Process: The script will capture up to 20 photos of detected faces. Press 'q' to stop capturing before reaching the limit.
Files: Captured images will be saved in the specified directory with filenames indicating the photo number.
Code Overview
Face Detection: The script uses OpenCV’s Haar Cascade for detecting faces in real-time.
Image Saving: Captures and saves frames where faces are detected, with file names including a photo counter.
Display and Control: Displays the live feed with detected faces highlighted and allows early exit by pressing 'q'.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

This README provides a clear overview of the script’s functionality, installation, usage, and contribution guidelines. Adjust any specific details as needed for your project.
