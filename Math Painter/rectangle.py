


# this file contains the rectangle class
class Rectangle:
    # constructor
    def __init__(self, x, y, width, height, color):
        self.color = color  # blue OR orange
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    # draw()
    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color
