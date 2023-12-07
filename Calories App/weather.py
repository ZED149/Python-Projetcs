


# this file contains the weather class

#importing libraries
import requests
from selectorlib import Extractor

class Weather:
    """
    This class contains country and city. It can scrap data from internet for the
    temperature in that city of country.
    """
    # constructor
    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def calculate_temperature(self, weather):
        """
        performs a scrap on internet to find temperature for a given location
        :param weather:
        :return:
        """
        # creating url
        url = "https://www.timeanddate.com/weather/" + weather.country + "/" + weather.city
        # doing a get request on the server
        r = requests.get(url)
        # now we have our source code in 'r'
        # converting it into a string format
        content = r.text

        # need to extract data from the source code
        # the data is to be extracted is the temp for the location
        e = Extractor.from_yaml_file("temperature.yaml")
        # doing search from our source code
        raw_result = e.extract(content)
        # raw_result is a python dictionary that contains our data
        result = raw_result['temp'].replace("\xa0°C", "")
        return float(result)