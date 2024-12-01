

# This file contains item.py class

# Item.py
class Item:
    i_name: str             # name of the item
    i_description: str      # description of the item
    i_weight: float           # weight of the item


    # Constructor
    def __init__(self, i_name: str, i_description: str, i_weight: float) -> None:
        self.i_name = i_name
        self.i_description = i_description
        self.i_weight = i_weight

    
    # Getters

    # getName
    def getName(self) -> str:
        """
        Returns:
            str: name of the item.
        """
        return self.i_name
    
    # getDescription
    def getDescription(self) -> str:
        """
        Returns:
            str: description of the item.
        """
        return self.i_description
    
    # getWeight
    def getWeight(self) -> float:
        """
        Returns:
            int: weight of the item.
        """
        return self.i_weight
    
    # Setters

    # setName
    def setName(self, i_name: str) -> None:
        """
        Args:
            i_name (str): name of the item
        """
        self.i_name = i_name

        # setDescription
    def setName(self, i_description: str) -> None:
        """
        Args:
            i_description (str): description of the item
        """
        self.i_name = i_description

        # setWeight
    def setName(self, i_weight: float) -> None:
        """
        Args:
            i_weight (int): weight of the item
        """
        self.i_name = i_weight

    def __str__(self):
        return f"{self.i_description}"

        