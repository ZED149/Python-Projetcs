# This file contains the Geometry game implemented using OOP concepts


# Point class
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

import turtle

# Rectangle class
class Rectangle:
    # Constructor
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # falls in rectangle
    def falls_in_rectangle(self, p):
        if (self.p1.x < p.x < self.p2.x
                and self.p1.y < p.y < self.p2.y):
            print("Yes, it falls in the Rectangle\n")
        else:
            print("No, it doesn't falls in rectangle\n")

    # calculate area
    def area(self):
        area = (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)
        print(f"Area is: {area}")

    # draw rectangle
    def draw_rectangle(self, mp):
        # this function will draw rectangle on the canvas
        mt = turtle.Turtle()    # creating an instance of canvas
        # now we need to move away from origin
        # but before moving we need to lift pen up
        mt.penup()  # this will lift the penup
        # now we can move without drawing any line
        mt.goto(self.p1.x, self.p1.y)

        # now we place pen down
        mt.pendown()
        # we can draw a rectangle now
        # before drawing lets just calculate width and height of our triangle
        width = self.p2.x - self.p1.x
        height = self.p2.y - self.p1.y
        # actually drawing now
        mt.forward(width)
        # rotating along 90 degrees
        mt.left(90)
        mt.forward(height)
        mt.left(90)
        mt.forward(width)
        mt.left(90)
        mt.forward(height)

        # now we need to draw our point on the canvas
        mt.penup()
        mt.goto(mp.x, mp.y)
        mt.pendown()
        mt.dot(5, "red")

        # wait before closing canvas window
        turtle.done()

    def __str__(self):
        return f"({self.p1.x}, {self.p1.y}), ({self.p2.x}, {self.p2.y})"

