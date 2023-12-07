


# this is the main for geometry application


from geometry import *
from random import randint

# creating some random integer from 1 - 1000
p1 = Point(randint(1, 250), randint(1, 250))
p2 = Point(randint(250, 500), randint(250, 500))

my_rec = Rectangle(p1, p2)
print(my_rec)
mp = Point(250,250)
my_rec.falls_in_rectangle(mp)
my_rec.area()
my_rec.draw_rectangle(mp)

