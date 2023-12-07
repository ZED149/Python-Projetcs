


# this is the main file for this program

# main()
# importing libraries
from user import User
from weather import Weather
from calories import *


# creating user
u1 = User(70, 175, 32)
u2 = User(20, 200, 43)

# creating weather
w = Weather("Pakistan", "Lahore")
w2 = Weather("USA", "Washington")
# creating Calorie
c = Calories()
a = c.calculates(u1, w2)
print(a)