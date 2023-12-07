


# this file contains the calories class

# importing libraries
from user import User
from weather import Weather

class Calories:
    """
    This class calculates calories useing
    BMR = 10*weight + 6.25* height -5*age +5 -10*temperature
    """
    # calculates
    def calculates(self, user, weather):
        """
        Calculates a user needed calories using BMR Formula
        :param user:
        :param weather:
        :return:
        """
        BMR = float((10*user.width) + (6.25*user.height) -(5*user.age) +5 - (10*weather.calculate_temperature(weather)))
        return BMR
