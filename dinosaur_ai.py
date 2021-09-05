import os
import tensorflow as tf
import cv2 as cv
import numpy as np
import keyboard
import time
from PIL import ImageGrab

model = tf.keras.models.load_model("saved_model")
labels = ["up", "down", "right"]

print("Model Loaded")
print("Waiting for spacebar keypress")

# Halts the script until the game is started.
keyboard.wait("space")

# Waits for the starting animation to end.
time.sleep(2)

print("Starting game")

while True:

    if keyboard.is_pressed("esc"):
        break

    image = ImageGrab.grab(bbox=(220, 350, 820, 750))
    cv_image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    grayscale = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY)

    normalized = grayscale / 255
    resized = cv.resize(normalized, (60, 40), interpolation=cv.INTER_AREA)

    probabilities = model.predict(np.array([np.ravel(resized)]))
    key = labels[np.argmax(probabilities)]

    print(key, np.max(probabilities))

    if key == "up" or key == "down":
        keyboard.press(key)
        keyboard.release(key)
