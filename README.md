# Hand Tracking Project

This project demonstrates the power of computer vision and hand tracking technology to create interactive applications. Using OpenCV and MediaPipe, we've developed two Python scripts: a basic hand tracking program and an innovative virtual piano controlled by hand gestures.

## Project Overview

The Hand Tracking Piano Project showcases how computer vision can be used to create intuitive, touchless interfaces. By leveraging the capabilities of OpenCV for image processing and MediaPipe for hand tracking, we've created a system that can detect and interpret hand movements in real-time.

### Technologies Used

- **OpenCV**: Used for capturing and processing video frames from the webcam.
- **MediaPipe**: Provides the hand tracking solution, allowing us to detect and track hand landmarks.
- **Python**: The primary programming language used for implementation.
- **Pygame**: Used in the piano application for audio playback.

## Scripts

### 1. main.py - Basic Hand Tracking

This script serves as a foundation for hand tracking applications. It demonstrates how to:

- Capture video input from a webcam using OpenCV
- Process each frame to detect hands using MediaPipe's hand tracking solution
- Visualize hand landmarks and connections in real-time

`main.py` is an excellent starting point for understanding how hand tracking works and can be used as a base for more complex applications.

### 2. piano.py - Virtual Piano Application

Building upon the hand tracking capabilities demonstrated in `main.py`, this script creates an interactive virtual piano. Key features include:

- Displaying virtual piano keys on the screen
- Using MediaPipe to track the position of the user's index finger
- Detecting when the index finger "presses" a key
- Playing corresponding piano notes using Pygame for audio output

`piano.py` showcases how hand tracking can be applied to create an engaging, touchless musical instrument.

## How It Works

1. **Video Capture**: OpenCV is used to capture video frames from the webcam.
2. **Hand Detection**: Each frame is processed using MediaPipe's hand tracking model to detect and locate hand landmarks.
3. **Gesture Interpretation**: In `piano.py`, the position of the index finger is tracked relative to the virtual piano keys.
4. **Visual Feedback**: OpenCV is used to draw the piano keys and provide visual feedback when keys are "pressed".
5. **Audio Playback**: When a key press is detected, Pygame plays the corresponding piano note.

This project demonstrates the potential of combining computer vision libraries like OpenCV with specialized machine learning models like those in MediaPipe to create intuitive, gesture-based interfaces.

## Future Enhancements

This project can serve as a starting point for more complex hand tracking applications. Potential enhancements could include:
- Multi-hand tracking for more complex interactions
- Integration with other musical instruments or controls
- Expansion into other domains like gesture-based gaming or sign language interpretation
