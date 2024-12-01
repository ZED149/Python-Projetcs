

# this file contains npc.py class
# npc ---> Non Player Character

# NPC class
class NPC:
    name: str               # name of the charcater
    spoken_phrase: str      # spoken phrase

    # Constructor
    def __init__(self, name: str, spoken_phrase: str) -> None:
        self.name = name
        self.spoken_phrase = spoken_phrase

    
    # Getters

    # getName
    def getName(self) -> str:
        """
        Returns:
            str: name of the npc
        """
        return self.name
    
    # getSpokenPhrase
    def getSpokenPhrase(self) -> str:
        """
        Returns:
            str: spoken phrase of the npc
        """
        return self.spoken_phrase
    
    # Setters

    # setName
    def setName(self, name: str) -> None:
        """
        Args:
            name (str): name of the npc
        """
        self.name = name

    # setSpokenPhrase
    def setSpokenPhrase(self, spokenPhrase: str) -> None:
        """
        Args:
            spokenPhrase (str): spoken phrase of the npc
        """
        self.spoken_phrase = spokenPhrase

    def __str__(self):
        return f"You meet {self.name}"
    
    # Methods

    # speak
    def speak(self) -> str:
        """
            Returns the name of the spoken phrase.
        Returns:
            str: name of the spoken phrase
        """
        return f'{self.name} says, "{self.spoken_phrase}!"'