

# This file contains the main of Restaurant Picker Program

# including some important libraries
from restaurant_picker import RestaurantPicker
from restaurant import Restaurant
from exit_codes import ExitCodes

# setting up the context


# utility function
def print_restaurants(restaurants: [Restaurant]) -> None:
    """
    Prints the list of restaurants. In case of no restaurants found, prints None.
    :param restaurants: List of restaurants.
    :return: None
    """
    # checking length of restaurants
    if len(restaurants) == 0:
        exit(ExitCodes.NO_RESTAURANT_FOUND)

    for r in restaurants:
        print(r)


# initializing the Restaurant Picker object
obj: RestaurantPicker = RestaurantPicker()
# loading restaurants from a file
obj.load_restaurants_from_file("restaurants.csv")
# printing available restaurants in a nice format
# obj.print_restaurants()

################################################
# after setting up the environment, we can start creating a menu for the user
# we need to ask the user for some of his preferences
country = input("Enter Your Country: ")
print("Fetching restaurants for: {country}".format(country=country))
# listing available restaurants
restaurant = obj.get_restaurant(attribute="country", value=country)
print_restaurants(restaurants=restaurant)

# now asking for which city he wants...
city = input("Enter the city you would like to eat... ")
restaurant = obj.get_restaurant(attribute="city", value=city)
print("Listing restaurants for: {city} in the {country}".format(city=city, country=country))
# listing available restaurants
print_restaurants(restaurants=restaurant)

# asking for address
location = input(f"Enter on which location of {city} would you like to eat? ")
restaurant = obj.get_restaurant(attribute="address", value=location)
print(f"Listing restaurants for location: {location}")
print_restaurants(restaurants=restaurant)

exit(ExitCodes.SUCCESS)
# END
