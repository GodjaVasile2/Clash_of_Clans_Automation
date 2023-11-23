import pyautogui
import keyboard
import time
from pynput import mouse


def get_rgb_color(x, y):
    return pyautogui.screenshot().getpixel((x, y))


def on_click(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 's':
        print("Script started. Press 'q' to exit.")

        def on_mouse_click(x, y, button, pressed):
            if pressed and button == mouse.Button.left:
                rgb_color = get_rgb_color(x, y)
                print(
                    f"Left click at coordinates: ({x}, {y}), RGB: {rgb_color}")

        # Set up the mouse listener
        mouse_listener = mouse.Listener(on_click=on_mouse_click)
        mouse_listener.start()

        try:
            while True:
                time.sleep(0.1)
                if keyboard.is_pressed('q'):
                    print("Script terminated by the user.")
                    break
        except KeyboardInterrupt:
            pass
        finally:
            # Stop the mouse listener
            mouse_listener.stop()
            mouse_listener.join()


# Set up the keyboard listener
keyboard.hook(on_click)

try:
    keyboard.wait('q')
except KeyboardInterrupt:
    pass
finally:
    print("Script exited.")
