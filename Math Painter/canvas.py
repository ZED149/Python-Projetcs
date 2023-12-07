


# this file contains the canvas class

#importing libraries
import numpy as np
from PIL import Image
class Canvas:
    # constructor
    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

        # creating a canvas of (x, y) coordinates
        # first create a 3D array of zeroes
        # width = x = horizontal
        # height = y = vertical
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        # replacing zeroes with color
        self.data[:] = self.color

    # make()
    def make(self, image_path):
        # now we have our desired color canvas
        # we need to convert this data array into an Image
        # converting array into image
        img = Image.fromarray(self.data, "RGB")

        # saving it on hard drive
        img.save(image_path)
