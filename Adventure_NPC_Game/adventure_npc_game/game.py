

# this file includes Game class


# importing important libraries
from .item import Item
from .npc import NPC
from .room import Room

# Game class
class Game:

    # Item's
    __magnifying_glass = None
    __notebook = None
    __steel_safe = None
    __flashlight = None

    # NPC's
    __inspector_grave = None
    __mysterious_women = None

    # Room
    __starting_room = None
    __dark_alley = None
    __abandoned_warehouse = None
    __hidden_room = None
    __city_hall = None
    __rooftop_garden = None
    __safe_vault = None
    __glamorous_penthouse = None

    # checking something
    __g_rooms = {
        "Detective's Office": None,
        "Dark Alley": None,
        "Abandoned Warehouse": None,
        "Hidden Room": None,
        "City Hall": None,
        "Rooftop Garden": None,
        "Safe Vault": None,
        "Glamorous Penthouse": None
    }

    # private data members
    __next = None


    m_items_list = []               # list of items that the player has been holding. These items have been taken along the way.
    m_room: Room                    # Room to store player's current location
    game_message = ""               # to maintain the current game message. Updated in alomst every method


    # Cosntructor
    def __init__(self, starting_location_game: Room, m_items_list: list = []):
        # Task 1
        self.m_items_list = m_items_list

        # Task 2
        self.create_world()

        # Task 3
        self.m_room = starting_location_game

        # Task 4
        self.set_welcome_message()

    
    # Getters

    # getMessage
    def getMessage(self) -> str:
        return self.game_message
    
    # getCurrentRoom
    def getCurrentRoom(self) -> Room:
        return self.m_room
    
    # Methods

    # create_World
    def create_world(self):
        # intializing item's
        self.__magnifying_glass = Item("Magnigying Glass", "You see a polished magnifying glass, perfect for examing clues.", 0.2)
        self.__notebook = Item("Notebook", "You see a worn notebook filled with scriblled notes and observations.", 0.5)
        self.__steel_safe = Item("Steel Safe", "You see a large steel safe, locked tight and far too heavy to move", 150)
        self.__flashlight = Item("Flashlight", "You see a sturdy flashlight, flickering but still functional.", 1)

        # intializing NPC's
        self.__inspector_grave = NPC("Inspector Graves", "Look closely detective. The smallest detail may lead to the biggest revealation.")
        self.__mysterious_women = NPC("Scarlet", "In this city trust is a rare commodity. Choose your allies wisely.")

        # initialzing Room's
        self.__g_rooms["Detective's Office"] = Room("Detective's Office", "You are in a cluttered office filled with case files and dim lighting.", m_item=self.__notebook, m_npc=self.__inspector_grave, adjacent_rooms={'south':'Dark Alley', 'east':'City Hall'})
        self.__g_rooms['Dark Alley'] = Room("Dark Alley", "You are in a narrow alley shrouded in shadows, with the sound of distant sirens.", m_item=self.__magnifying_glass, adjacent_rooms={'north': "Detective's Offce", "west": "Abandoned Warehouse"})
        self.__g_rooms['Abandoned Warehouse'] = Room("Abandoned Warehouse", "You are inside a dusty warehouse filled with old crates and cobwebs", adjacent_rooms={'east': "Dark Alley", 'south': "Hidden Room"})
        self.__g_rooms['Hidden Room'] = Room("Hidden Room", "You are in a hidden room behind a false wall, filed with stolen goods.", adjacent_rooms={'north': "Abandoned Warehouse", "east": "Safe Vault"})
        self.__g_rooms['City Hall'] = Room("City Hall", "You are in the grand hall of the city, with marble floors and soaring ceilings.", adjacent_rooms={'west': "Detective's Office", "south": "Rooftop Garden"})
        self.__g_rooms['Rooftop Garden'] = Room("Rooftop Garden", "You are in a serence garden on the rooftop, overlooking the city skyline.", adjacent_rooms={'north': "City Hall"})
        self.__g_rooms['Safe Vault'] = Room("Safe Vault", "You are in a secure vault with a massive steel safe and various survelliance equipment.", adjacent_rooms={"west": "Hidden Room"})
        self.__g_rooms['Glamorous Penthouse'] = Room("Galmorous Penthouse", "You are in a lavish penthouse, adorned with expensive decor and art.", adjacent_rooms={'south': "City Hall"})
        

    # move
    def move(self, dir):
        self.__next = self.m_room.getNeighbour(dir)
        if self.__next == None:
            self.game_message = "You can't move in that direction"
        else:
            self.m_room = self.__g_rooms[self.__next]
            self.game_message = self.m_room.__str__()
            # a = 1

    
    # set_welcome_message
    def set_welcome_message(self):
        self.game_message = """You are an elite detective in the bustling city of Noirville, trying to solve the mysterious
disappearance of a famous jewel called the "Midnight Star." As you navigate through the dark
alleys, hidden rooms, and upscale penthouses, you must gather clues, interact with suspicious
characters, and piece together the mystery before time runs out. The clock is ticking, and every
choice you make could lead you closer to solving the case or falling into a trap."""


    # parse_command
    def parse_command(self):
        """prompt the player for command and return 2 strings, with the second one as optional
        """
        words = input("Enter>>>").split()
        # words = ["move", "south"]
        first = words[0]
        if len(words) > 1:
            second = words[1]
        else:
            second = None
        return first, second

    
    # play
    def play(self):
        # printing initial welcome message
        print(self.getMessage())

        # looping until game over
        while True:
            first, second = self.parse_command()
            if first == "move":
                self.move(second)
            elif first == "look":
                self.look()
            elif first == "help":
                self.help()
            elif first == "items":
                self.items()
            elif first == "take":
                self.take()
            elif first == "place":
                self.place()
            elif first == "search":
                self.search_items("")
            elif first == "speak":
                self.speak()
            if self.game_over():
                print(self.getMessage())
                break
            print(self.getMessage())
            
    

    # look
    def look(self):
        """updates the game message with the current room's description
        """
        self.game_message = self.m_room.__str__()

    
    # help
    def help(self):
        """updates the game's message with hints suggestions and reminders about the game objective.
        """
        self.game_message = "You are lost and alone. Find three magic gems and shout the magic phrase to escape."

    
    # items
    def items(self):
        """updates the game's message with 
        1. a list of all items the player is holding.   OR
        2. a message indicating that the player is not holding anything.
        """
        if len(self.m_items_list) <= 0:
            self.game_message = "You are holding nothing."
            return
        self.game_message = 'You are holding:\n'
        for index, _item in enumerate(self.m_items_list):
            self.game_message = self.game_message + f"{index + 1}. {_item}\n"

    
    # take
    def take(self):
        """if appropriate, remove the item from the current location and add it to the list of items.
        Update the game message with one of the following options:
        1. there is no item here to take
        2. the item is too heavy(50 units)
        3. the player is now holding the item.
        """
        # check in the room for items
        if self.m_room.getItem() and (self.m_room.getItem().getWeight() < 50):
            # updating the game message
            self.game_message = f"You are holding a {self.m_room.getItem()}."
            # adding the item to the player's item list
            self.m_items_list.append(self.m_room.getItem())
            # removing item from the room
            self.m_room.setItem(None)
        elif self.m_room.getItem() and (self.m_room.getItem().getWeight() >= 50):
            self.game_message = "The treasure is too heavy to pick up!"
        elif self.m_room.getItem() == None:
            self.game_message = "There is nothing to take."

        
    # place
    def place(self):
        """if appropraite, remove the item from the list of help items and place it into the current room.
        """
        if (len(self.m_items_list) <= 0):
            self.game_message = "You are not holding a anything."
        elif self.m_room.getItem():
            self.game_message = "There is already an item in the room."
        elif self.m_room.getItem() == None:
            # place the item in the room and removing it at the same time
            self.m_room.setItem(self.m_items_list.pop())


    # search_items
    def search_items(self, name):
        """
        check the list of help items by the name.
        """
        if self.m_room.getItem():
            self.game_message = self.m_room.getItem()
        else:
            self.game_message = "No items present in the room."
            
    
    # speak
    def speak(self):
        """Updates the game's message with one of the following options.
        1. The room has no NPC
        2. the NPC's spoken phrase
        """
        # check for an NPC in the current room
        if self.m_room.getNPC() == None:
            self.game_message = "There is no one here to speak."
        elif self.m_room.getNPC():
            self.game_message = 'Frodo says, "Seek and you will find."'

        
    # game_over
    def game_over(self) -> bool:
        """determine if the game is over because the player has either lost or won.
        """
        if (self.m_room.getName() == "Glamorous Penthouse") and (self.m_items_list[0] == 'Midnight Star Jewel'):
            self.game_message = "Player Wins!"
            return True
        elif ((self.m_room.getName() == "City Hall") and (self.m_items_list)):
            if "Notebook" == self.m_items_list[0].getName():
                self.game_message = "Player Wins!"
                return True
            
            