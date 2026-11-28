# OpenCV Practice

This repository contains my OpenCV learning exercises and computer vision projects developed using Python.

The goal is to practice image processing techniques and build practical computer vision applications.

## Technologies

- Python
- OpenCV
- NumPy
- Pillow

## Topics Covered

- Reading and displaying images and videos
- Webcam operations
- Image resizing and cropping
- Color spaces (BGR, RGB, HSV)
- Image masking and color detection
- Contour detection
- Shape recognition
- Bounding boxes and center coordinates
- Basic object tracking
- Image processing and visualization

## Projects

### 1. Color Detection

A simple application that detects a selected color using HSV color ranges.

**Features:**
- Real-time color detection
- HSV color filtering
- Bounding boxes around detected objects

### 2. Smart Object Tracker

A real-time computer vision application that detects colored objects, recognizes their shapes, and visualizes their movement.

**Features:**
- Detection of green, blue, and yellow objects
- Shape recognition (circle, triangle, square, rectangle)
- Bounding boxes and object labels
- Object center coordinates
- Motion trails based on detected positions
- Saving processed camera frames as images

The tracking system uses color detection and position history rather than a trained object detection model.

## Installation

Install the required Python libraries:

`python3.13 -m pip install opencv-python numpy pillow`

## Usage

Clone or download the repository, open it in VS Code, and run the desired Python file.

To run Smart Object Tracker from the repository root:

`python3.13 Projects/Smart-Object-Tracker/main.py`

**Controls:**
- `S` — Save the current frame
- `Q` — Quit the application

Make sure your webcam is connected and camera permissions are enabled.

## Future Improvements

- Improve detection under different lighting conditions
- Reduce false detections
- Explore more advanced object tracking techniques
- Experiment with YOLO-based object detection

## Purpose

This repository documents my progress in learning computer vision and developing practical image processing skills.
