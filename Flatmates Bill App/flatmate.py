# FlatMate class
class Flatmate:
    """
    It creates a Flatmate object which contains its name, days_in_house.
    """

    # Constructor
    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    # pays()
    def pays(self, bill, flatmate2):
        """
        This function returns the exact amount that is needed to be paid by the caller flatmate
        :param bill:
        :param flatmate2:
        :return:
        """

        total_days_in_house = self.days_in_house + flatmate2.days_in_house
        percentage = self.days_in_house / total_days_in_house

        return percentage * bill.amount

