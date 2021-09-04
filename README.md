# Chrome Dinosaur Game AI with Neural Networks

chrome://dino/

## Gathering Your Own Training Data

If you'd like to run the `get_training_data.py` script and create your own training data, do the following:

1. Open chrome://dino/ (make sure it's in full browser and on your main display)
2. Run the script.
3. Press space when you're ready to start the game.
4. Play the game (try to press keys only when necessary to obtain more accurate screenshots since it's dependent on your action)
5. Once the game is over, press escape to stop the script (you may need to manually remove excess images that are of the game over screen)

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
