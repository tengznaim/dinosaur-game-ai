from PIL import ImageGrab
import os
import keyboard
import time

parent_dir = os.getcwd()
training_data_folder = os.path.join(parent_dir, "training_data")
up_folder = os.path.join(training_data_folder, "up")
down_folder = os.path.join(training_data_folder, "down")
right_folder = os.path.join(training_data_folder, "right")

if "training_data" not in os.listdir(parent_dir):
    os.mkdir(training_data_folder)
    os.mkdir(up_folder)
    os.mkdir(down_folder)
    os.mkdir(right_folder)

up_count = len(os.listdir(up_folder))
down_count = len(os.listdir(down_folder))
right_count = len(os.listdir(right_folder))

print("Waiting for spacebar keypress")

# Halts the script until the game is started.
keyboard.wait("space")

# Waits for the starting animation to end.
time.sleep(2)

print("Starting to take screenshots")

while True:
    # Exit key to stop taking screenshots.
    if keyboard.is_pressed("esc"):
        break

    elif keyboard.is_pressed("up") and up_count < 1000:
        image = ImageGrab.grab(bbox=(220, 350, 820, 750))
        image_name = f"up({up_count}).png"
        image.save(os.path.join(up_folder, image_name))
        up_count += 1

    elif keyboard.is_pressed("down") and down_count < 1000:
        image = ImageGrab.grab(bbox=(220, 350, 820, 750))
        image_name = f"down({down_count}).png"
        image.save(os.path.join(down_folder, image_name))
        down_count += 1

    elif right_count < 1000:
        image = ImageGrab.grab(bbox=(220, 350, 820, 750))
        image_name = f"right({right_count}).png"
        image.save(os.path.join(right_folder, image_name))
        right_count += 1

    # Modifiable, used to prevent taking too many screenshots before the screen has changed.
    time.sleep(0.1)

print("----------Training Data Summary----------")
print("Up Images:", up_count)
print("Down Images:", down_count)
print("Right Images:", right_count)
