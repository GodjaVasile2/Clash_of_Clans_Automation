
import cv2
import numpy as np
import pyautogui
import time
import random
import easyocr
from ultralytics import YOLO


def click_button(max_loc, template_img, random_offset=False, delay_after_click=1):
    x, y = max_loc

    image_width = template_img.shape[1]
    image_height = template_img.shape[0]

    center_x = x + template_img.shape[1] // 2
    center_y = y + template_img.shape[0] // 2

    if random_offset:
        center_x = random.randint(x, x + image_width)
        center_y = random.randint(y, y + image_height)

    pyautogui.click(center_x, center_y)
    time.sleep(delay_after_click)


def find_template(template_path, threshold, delay_after_click, random_offset=False):

    screenshot = pyautogui.screenshot()
    screenshot.save('attack_resources/temp_screenshot.png')
    screenshot_img = cv2.imread(
        'attack_resources/temp_screenshot.png', cv2.IMREAD_UNCHANGED)
    template_img = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(
        screenshot_img, template_img, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        click_button(max_loc, template_img,
                     random_offset=random_offset, delay_after_click=delay_after_click)
        return True
    else:
        print(f"{template_path} Button not found.")
        return False


def extract_resources():

    screenshot_pil = pyautogui.screenshot()
    screenshot_np = np.array(screenshot_pil)
    resources_img = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    resource_region = resources_img[32:250, 32:800]
    resource_region_rgb = cv2.cvtColor(resource_region, cv2.COLOR_BGR2RGB)

    reader = easyocr.Reader(['en'])
    result = reader.readtext(resource_region_rgb)

    extracted_text = [detection[1] for detection in result]

    try:
        resouces = map(lambda x: int(x.replace(' ', '')),
                       extracted_text[-3:-1])
        gold, elixir = resouces
    except ValueError as e:
        print(f"Error: {e}")
        gold, elixir = 0, 0

    return gold, elixir


def prepare_troops():
    # i will use just click positions and i hope that the buttons are there
    # this functio will work only on 1080p resolution ( i think )

    # TO DO: add the function to detect the buttons using the template matching
    # click on the button to prepare troops
    pyautogui.click(69, 832)
    # click on the quick train button
    pyautogui.click(1206, 74)
    # click on the train button
    pyautogui.click(1644, 508)


def deploy_troops(village_img):

    # i have to identify the green zones where i can deploy the troops as close as posible to the detected resources
    # identify the position of the resources

    pyautogui.click(338, 992)

    yolo_model = YOLO("best.pt")
    results = yolo_model(village_img, save=True, conf=0.40)
    for element in results:
        for box in element.boxes.xyxy:
            x_min, y_min, x_max, y_max = box[:4].cpu().numpy()

            acceptable_colors = [(159, 178, 75), (178, 194, 73)]

            closest_point = find_closest_pixel_outside_rectangle(
                x_min, y_min, x_max, y_max, acceptable_colors, min_distance=4)

            if closest_point is not None:
                deploy_x, deploy_y = closest_point
                print(f"Deploying troops at {deploy_x}, {deploy_y}.")
                # pyautogui.click(deploy_x, deploy_y)
            else:
                print("No suitable pixel found for deployment.")
                pass

            # click on the troop from the bar
            # select barbarian troop

            pyautogui.click(deploy_x, deploy_y)

            # select archer troop
            # click on the closest green zone to the resource

# x_min is the minimum x-coordinate (the leftmost point of the rectangle).
# y_min is the minimum y-coordinate (the topmost point of the rectangle).
# x_max is the maximum x-coordinate (the rightmost point of the rectangle).
# y_max is the maximum y-coordinate (the bottommost point of the rectangle).


def find_closest_pixel_outside_rectangle(x_min, y_min, x_max, y_max, acceptable_colors, min_distance=5):
    screenshot = pyautogui.screenshot()
    closest_point = None
    min_distance_outside = float('inf')

    x_min, y_min, x_max, y_max, min_distance = map(
        int, (x_min, y_min, x_max, y_max, min_distance))

    # Define the search area to be outside the rectangle at a minimum distance of 5 pixels
    search_x_min = max(0, x_min - min_distance)
    search_y_min = max(0, y_min - min_distance)
    search_x_max = min(screenshot.width, x_max + min_distance)
    search_y_max = min(screenshot.height, y_max + min_distance)

    for x in range(search_x_min, search_x_max + 1):
        for y in range(search_y_min, search_y_max + 1):
            # Skip pixels inside the rectangle
            if x_min <= x <= x_max and y_min <= y <= y_max:
                continue

            color = screenshot.getpixel((x, y))
            if color in acceptable_colors:
                distance = np.sqrt((x - x_min)**2 + (y - y_min)**2)
                if distance < min_distance_outside:
                    min_distance_outside = distance
                    closest_point = (x, y)

    return closest_point


def main():

    time.sleep(2)

    # find the attack button
    find_template('attack_resources/attack_btn.png',
                  threshold=0.8, delay_after_click=1, random_offset=True)
    # find the find a match button
    find_template('attack_resources/find_a_match_btn.png', threshold=0.8,
                  delay_after_click=4, random_offset=True)

    while True:

        gold, elixir = extract_resources()

        # TO DO add the dark elixir to the ecuation
        # TO DO manage cases when the last element is gold

        if gold > 250000 and elixir > 250000:

            screenshot = pyautogui.screenshot()

            # save the enemy_base image in order to detect the resources
            screenshot.save('attack_resources/village.png')
            village_img = cv2.imread(
                'attack_resources/village.png', cv2.IMREAD_UNCHANGED)

            # deploy the troops based on the location of the resources
            deploy_troops(village_img)

        else:
            print(
                f"The player is poor! Available resources: {gold} gold and {elixir} elixir.")

            # find the next button
            find_template('attack_resources/next_btn.png', threshold=0.8,
                          delay_after_click=4, random_offset=True)


if __name__ == "__main__":
    main()
