

# This file contains the Restaurant class

class Restaurant:
    # private data members
    __name = ""                 # name of the restaurant
    __address = ""              # address of the restaurant
    __city = ""                 # city of the restaurant
    __country = ""              # country of the restaurant
    __rating = int              # rating of the restaurant [0 - 5], 0=worst, 5=best
    __music_allowed = bool      # either music is allowed in the restaurant or not
    __parking_space = int       # number of parks to be parked in the restaurant at a time
    __cuisine = ""              # cuisine of restaurant
    __price_range = ""          # price range of the restaurant

    # Constructor
    def __init__(self, name: str, address: str, city: str, country: str,
                 rating: int, music_allowed: bool, parking_space: int, cuisine: str, price_range: str) -> None:
        """
        Initialize the restaurant object based on its parameters.
        :param name: Name of the restaurant
        :param address: address of the restaurant
        :param city: city of the restaurant
        :param country: country of the restaurant
        :param rating: rating of the restaurant [1 - 5], 0=worst, 3=average, 5=best
        :param music_allowed: either music is allowed or not
        :param parking_space: total number of vehicle's to be parked at a time
        :param cuisine: cuisine of the restaurant
        :param price_range: price range of the restaurant
        """

        # assigning values to the private variables
        self.__name = name
        self.__address = address
        self.__city = city
        self.__country = country
        self.__rating = rating
        self.__music_allowed = music_allowed
        self.__parking_space = parking_space
        self.__cuisine = cuisine
        self.__price_range = price_range

    # Member Functions

    # load_from_file
    def load_from_file(self, filename) -> bool:
        raise NotImplemented("Needs to be implemented.")

    @classmethod
    # attributes
    def attributes(cls) -> tuple:
        """
        Returns a Tuple of the attributes of the restaurant.
        :return:
        """
        return "name", "address", "city", "country", "rating", "music_allowed", "parking_space", "cuisine", "price_range"

    # Operator Overloading

    def __str__(self):
        constructed_string = "----------------------------------------------------------------------\n"
        constructed_string = constructed_string + f"Name: {self.__name}\nAddress: {self.__address}\nCity: {self.__city}\nCountry: {self.__country}\n"
        constructed_string = constructed_string + f"Rating: {self.__rating}\nMusic Allowed: {self.__music_allowed}\nParking Space: {self.__parking_space}\n"
        constructed_string = constructed_string + f"Cuisine: {self.__cuisine}\nPrice Range: {self.__price_range}\n"
        constructed_string = constructed_string + "----------------------------------------------------------------------"
        return constructed_string

    # Getters

    # get city
    def get_city(self) -> str:
        """
        Returns the city of the restaurant.
        :return:
        """
        return self.__city

    # get country
    def get_country(self) -> str:
        """
        Returns the country of the restaurant.
        :return:
        """
        return self.__country

    # get address
    def get_address(self) -> str:
        return self.__address
