


# this file contains the main() for math_painter app

# importing libraries
from canvas import Canvas
from square import Square
from rectangle import Rectangle


# making a canvas
my_canvas = Canvas(1440, 2560, color=(255, 255, 255))

# making a square
sq = Square(0, 0, 1, (0, 100, 222))
#sq.draw(my_canvas)

# making a rectangle
rec = Rectangle(3, 5, 600, 800, (100, 200, 125))
#rec.draw(my_canvas)

ez = 0
for i in range(1441):
    for j in range(2561):
        if ez == 256:
            ez = 0
        sq.x = i
        sq.y = j
        sq.color = (36, ez, 0)
        sq.draw(my_canvas)
        ez = ez + 1



my_canvas.make("files\\my_canvas.png")
