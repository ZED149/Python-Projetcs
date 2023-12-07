# Bill class
class Bill:
    """
    It contains the bill object which contains its amount for that particular period.
    """

    # Constructor
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount

