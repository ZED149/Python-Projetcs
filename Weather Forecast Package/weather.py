# this file contains the weather class

# importing libraries
import requests


class Weather:
    """
    This class creates an object which can call methods to find data
    related to a specific country or city.
    """

    # constructor
    def __init__(self, api_key=None, city=None, lat=None, lon=None):

        # checking if city, lat and lon all are None
        if not city and not lat and not lon:
            raise TypeError("Too few arguments")
        # checking if api_key is provided or not
        if not api_key:
            raise TypeError("Please provide an API key.")

        self.__response = None
        if (lat is None) and (lon is None):
            # make request based on lat and lon
            self.__response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?appid={api_key}&"
                                           f"units=metric&"
                                           f"q={city}")
        else:
            # make query based on city
            self.__response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?appid={api_key}&"
                                           f"units=metric&"
                                           f"lat={lat}&"
                                           f"lon={lon}")

        # storing data in JSON format for future use
        self.__data = self.__response.json()

        # checking to proceed only if response code is 200 (success)
        if self.__response.status_code != 200:
            raise ValueError(f"{self.__data['message']}")

    # next_12h()
    def next_12h(self):
        """
        This function returns the JSON format of data object from request on the server.
        :return self.__data['list']:
        """
        # first check for response code
        if self.__response.status_code == 200:
            # returning forecast data of next 12 hrs
            return self.__data['list'][:4]
        else:
            raise TypeError("Please check object initialization arguments")

    # next_12h_simplified()
    def next_12h_simplified(self):
        """
        This function will return a simplified version of forecast data
        which will contain date, temp, and weather details.
        :return simplified_data:
        """

        # checking for response code in url
        if self.__response.status_code == 200:
            simplified_data = []
            for data in self.__data['list'][:4]:
                # iterating only first four items of list
                simplified_data.append((data['dt_txt'], data['main']['temp'], data['weather'][0]['description']))

            # returning
            return simplified_data
        else:
            raise TypeError("Please check object initialization arguments.")

    # icon
    def icon(self):
        """
        This function will return the icon for that present weather condition at that particular
        location.
        :return:
        """

        # constructing url with current weather condition
        current_weather_condition = self.__data['list'][0]['weather'][0]['icon']
        url = f"https://openweathermap.org/img/wn/{current_weather_condition}@2x.png"
        icon = requests.get(url)
        image = icon.content
        with open("image.png", "wb") as f:
            f.write(image)
