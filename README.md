# COC-Automations-with-OpenCV

## Description

 A collection of simple scripts for automating resource collection and enemy base scanning in the old but beloved strategy game, Clash of Clans. Developed by a beginner for personal use and learning.
 
## Functionalities

- **Template Matching:** Utilizes OpenCV for template matching to identify and interact with in-game buttons and resources.
  
- **OCR (Optical Character Recognition):** Extracts resource information from the game screen using EasyOCR.

- **Randomized Clicking:** Introduces randomness in clicking coordinates to avoid repetitive actions in the same spot.

- **Dynamic Thresholding:** Allows the adjustment of matching thresholds for different functionalities.

- **Enemy Base Analysis:** Scans for potential enemy bases with a minimum specified amount of loot.

- **Attack Functionalities (Under Development):** Recognizes loot numbers and their positions on the screen. Full attack functionalities are still in development.

## Usage

1. Install the required libraries using `pip install -r requirements.txt`.
2. Run the script with `python script_name.py`.
3. Follow the on-screen prompts and adjustments.

## Requirements

- Python 3.x
- OpenCV
- PyAutoGUI
- EasyOCR
- NumPy
- PIL (Pillow)

## Notes

- This project is developed by a beginner for educational purposes.
- Feel free to customize and enhance the script according to your needs.

## Acknowledgments

- Inspired by ClarityCoders and Kian Brose.

