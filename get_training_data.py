from PIL import ImageGrab
import os
import keyboard
import time

parent_dir = os.getcwd()
training_data_folder = os.path.join(parent_dir, "training_data")
up_folder = os.path.join(training_data_folder, "up")
down_folder = os.path.join(training_data_folder, "down")
right_folder = os.path.join(training_data_folder, "right")

up_count = len(os.listdir(up_folder))
down_count = len(os.listdir(down_folder))
right_count = len(os.listdir(right_folder))

keyboard.wait("space")

# 220, 750
# 600w, 400h
while True:
    if keyboard.is_pressed("esc"):
        break

    elif keyboard.is_pressed("up"):
        image = ImageGrab.grab(bbox=(220, 350, 820, 750))
        image_name = f"up({up_count}).png"
        image.save(os.path.join(up_folder, image_name))
        up_count += 1

    elif keyboard.is_pressed("down"):
        image = ImageGrab.grab(bbox=(220, 350, 820, 750))
        image_name = f"down({down_count}).png"
        image.save(os.path.join(down_folder, image_name))
        down_count += 1

    else:
        image = ImageGrab.grab(bbox=(220, 350, 820, 750))
        image_name = f"right({right_count}).png"
        image.save(os.path.join(right_folder, image_name))
        right_count += 1

    # Modifiable, used to prevent taking too many screenshots before the screen has changed.
    time.sleep(0.1)

image = ImageGrab.grab()
image.show()
