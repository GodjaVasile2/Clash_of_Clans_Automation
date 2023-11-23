import cv2
import pyautogui
import time
from ultralytics import YOLO
import random


def click_resource(x_min, y_min, x_max, y_max, random_offset=False):

    x = int(x_min + (x_max - x_min) / 2)
    y = int(y_min + (y_max - y_min) / 2)

    pyautogui.click(x, y)
    print(f"Clicked at {x}, {y}")

    time.sleep(0.5)

    if random_offset:

        x = random.randint(int(x_min), int(x_max))
        y = random.randint(int(y_min), int(y_max))

        pyautogui.click(x, y)
        print(f"Clicked at {x}, {y}")

        time.sleep(0.5)


def find_and_collect_resources(yolo_model, threshold):

    screenshot = pyautogui.screenshot()
    screenshot.save('resources/village.png')
    village_img = cv2.imread('resources/village.png', cv2.IMREAD_UNCHANGED)

    results = yolo_model(village_img, save=True, conf=threshold)

    for element in results:

        print(element.names)
        print(element.boxes.xyxy)
        for box in element.boxes.xyxy:
            x_min, y_min, x_max, y_max = box[:4].cpu().numpy()

            click_resource(x_min, y_min, x_max, y_max, random_offset=True)


def main():
    time.sleep(3)

    # load the model
    yolo_model = YOLO("best.pt")
    find_and_collect_resources(yolo_model, threshold=0.40)


if __name__ == "__main__":
    main()
