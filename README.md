# COC-Automations-with-Yolov8 and OpenCV

## Description

This project comprises a set of Python scripts for automating tasks in Clash of Clans wich is one of my childhood game. It uses computer vision and machine learning techniques, leveraging OpenCV, PyAutoGUI, and EasyOCR, to interact with the game environment. The primary focus is on resource collection and enemy base analysis. This project is for educational and exploratory purposes.

## Demo Video

Watch the demo of the project here: [Demo Video](demo.mp4)

## Functionalities

- **Resource Collection Automation:** Automates resource collection in the village using YOLO for object detection and PyAutoGUI for screen interactions.
  
- **Enemy Base Scouting:** Analyzes enemy bases to assess attack feasibility based on available resources.

- **Template Matching:** Utilizes OpenCV for matching in-game elements with predefined templates.

- **Optical Character Recognition (OCR):** Uses EasyOCR to extract and interpret text information from the game screen.

- **Randomized Click Patterns:** Implements random click actions to mimic human interaction and avoid pattern detection.

- **YOLO Object Detection:** Employs YOLO (You Only Look Once) for real-time object detection, identifying game elements such as resources and defenses.

## Usage

1. Install Python 3.x on your system.
2. Clone the repository to your local machine.
3. Install the required dependencies: `pip install -r requirements.txt`.
4. Train your custom model using the datasets provided in the `resources` and `defences` folders.You can do this by following the steps presented in train.py script
5.Modify the path in the script to your custom-trained model
6. Run the desired script: `python script_name.py`.
7. Adjust script parameters based on your screen resolution and game layout.

## Requirements

- Python 3.x
- OpenCV
- PyAutoGUI
- EasyOCR
- NumPy
- YOLO (Ultralytics)
- PIL (Python Imaging Library)

## Notes

*This project is developed for educational purposes.
*Effectiveness may vary with game updates, screen resolutions, and other factors.
*Scripts are designed for a specific game layout and might need adjustments for different setups.

