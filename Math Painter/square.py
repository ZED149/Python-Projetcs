


# this file contains the square class
class Square:
    # constructor
    def __init__(self,x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    # draw()
    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
