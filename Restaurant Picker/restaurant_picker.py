# This file contains the Restaurant Picker class

# importing some important libraries and classes
from restaurant import Restaurant
import pandas as pd


class RestaurantPicker:
    # private data members
    __restaurant_names_list: list = []

    # Constructor
    def __init__(self):
        """
        Initializes the restaurant picker object.
        """
        pass

    # Member Functions

    # load restaurants from file
    def load_restaurants_from_file(self, filename: str) -> bool:
        """
        Loads the restaurant_names_list from the given filename.
        Returns True if the process is successful else false.
        :param filename: Name of the file containing the restaurant details
        :return:
        """

        try:
            # opening the file using pandas and initializing data frame object
            df = pd.read_csv(filename)
            # iterating over the data frame object
            # while iterating, we populate our restaurant_names_list
            for index, row in df.iterrows():
                # initializing a temp restaurant object
                temp_restaurant: Restaurant = Restaurant(
                    row["name"], row["address"], row["city"], row["country"],
                    row["rating"], row["music_allowed"], row["parking_space"],
                    row["cuisine"], row["price_range"]
                )
                # appending the list
                self.__restaurant_names_list.append(temp_restaurant)
        except:
            return False
        # in case if try block didn't throw any exception.
        return True

    # print
    def print_restaurants(self):
        """
        Prints the entire restaurant_names_list in a nice format.
        :return:
        """
        # printing
        for index, restaurant in enumerate(self.__restaurant_names_list):
            print(f"{index} {restaurant}")

    # get restaurants
    def get_restaurant(self, attribute: str, value: str):
        """
        Returns the restaurants for the specified value.
        :param value: value on which to be searched for the restaurant.
        :param attribute: Attribute name of the Restaurant.
        :return:
        """

        # validating attribute
        if not attribute in Restaurant.attributes():
            raise KeyError(f"Attribute {value} not found.")

        # in case our attribute exists
        temp: [Restaurant] = []
        match attribute:
            case "city":
                for restaurant in self.__restaurant_names_list:
                    if restaurant.get_city() == value:
                        temp.append(restaurant)
            case "country":
                for restaurant in self.__restaurant_names_list:
                    if restaurant.get_country() == value:
                        temp.append(restaurant)
            case "address":
                for restaurant in self.__restaurant_names_list:
                    if restaurant.get_address() == value:
                        temp.append(restaurant)

        # returning list of fetched restaurants from the DB.
        return temp
