
# this is the main() for this program

import weather
from pprint import pprint

w = weather.Weather(api_key="9b108ce6779462af85ffa5611ba9d19f", city="lahore")
print(w.next_12h_simplified())
w.icon()
