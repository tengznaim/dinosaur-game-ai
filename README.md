# Chrome Dinosaur Game AI with Neural Networks

This is a densely connected artificial neural network trained to play the famous [Chrome dinosaur game](chrome://dino). I initially planned to implement this with a convolutional neural network, however, taking a step back to what I already knew, I was curious to see how well a regular ANN would work given such a task.

## Network Architecture

The NN is a 3 layer densely connected neural network.

- The input layer has 2400 units corresponding to a 60x40 image of the processed screenshot passed into the network.
- The hidden layer has 100 units (at this point it was just a random choice)
- The output layer has 3 units corrensponding to the possible game moves to make: up, down or right.

## Gathering Your Own Training Data

If you'd like to run the `get_training_data.py` script and create your own training data, do the following:

1. Open chrome://dino/ (make sure it's in full browser and on your main display)
2. Run the script.
3. Press space when you're ready to start the game.
4. Play the game (try to press keys only when necessary to obtain more accurate screenshots since it's dependent on your action)
5. Once the game is over, press escape to stop the script (you may need to manually remove excess images that are of the game over screen)

## Limitations

1. Running the game, either for obtaining training data or actually using the AI is only possible on the main display (eg. the laptop screen instead of an external display)
2. My browser is in dark mode and that's how the game starts off. I don't currently know if it works well during the day time mode of the game.

## References

1. Getting screenshots in Python

   - https://pillow.readthedocs.io/en/stable/reference/index.html
   - http://chayanvinayak.blogspot.com/2013/03/bounding-box-in-pilpython-image-library.html

2. Screenshotting an image and using it with OpenCV without saving

   - https://www.pyimagesearch.com/2018/01/01/taking-screenshots-with-opencv-and-python/

3. Working with the Sequential model and training parameters in Tensorflow

   - https://www.youtube.com/watch?v=MQD1yMnZ_jk
   - https://www.youtube.com/watch?v=_8Bydxud1XU
   - https://www.tensorflow.org/guide/keras/train_and_evaluate

4. The softmax activation function for the output layer
   - https://deepai.org/machine-learning-glossary-and-terms/softmax-layer
