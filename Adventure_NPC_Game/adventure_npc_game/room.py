

# this file contains room.py class

from .item import Item
from .npc import NPC

class Room:
    r_name: str                         # name of the room
    r_description: str                  # a description of the current location
    m_item: Item                        # Item
    m_npc: NPC                          # NPC
    adjacent_rooms: dict                # a dict of all adjacent rooms, keys => direction AND values => room


    # Constructor
    def __init__(self, r_name: str, r_description: str, adjacent_rooms: dict = None, m_item: Item = None, m_npc: NPC  = None) -> None:
        self.r_name = r_name
        self.r_description = r_description
        self.m_item = m_item
        self.m_npc = m_npc
        self.adjacent_rooms = adjacent_rooms

    
    # Getters

    # getName
    def getName(self) -> str:
        return self.r_name

    # getDescription
    def getDescription(self) -> str:
        return self.r_description
    
    # getItem
    def getItem(self) -> Item:
        return self.m_item
    
    # getNPC
    def getNPC(self) -> NPC:
        return self.m_npc
    
    # getNeighbour
    def getNeighbour(self, dir):
        try:
            return self.adjacent_rooms[dir] if self.adjacent_rooms[dir] else None
        except KeyError:
            return None
    
    # Setters

    # setDescription
    def setDescription(self, description: str) -> None:
        self.r_description = description

    # setItem
    def setItem(self, item: Item) -> None:
        self.m_item = item

    # setNPC
    def setNPC(self, npc: NPC) -> None:
        self.m_npc = npc

    # Methods

    # has_item
    def has_item(self) -> bool:
        return True if self.m_item else False
    
    # has_npc
    def has_npc(self) -> bool:
        return True if self.m_npc else False
    
    # add_neighbour
    def add_neighbour(self, direction, room) -> None:
        self.adjacent_rooms[direction] = room

    # remove_item
    def remove_item(self):
        temp: Item = self.m_item
        self.m_item =None
        return temp
    
    def __str__(self) -> str :
        formated_string = f"{self.r_description}.\n"
        if self.m_item:
            formated_string = formated_string + f"{self.m_item.__str__()}.\n"
            if self.m_npc:
                formated_string = formated_string + f"{self.m_npc.__str__()}.\n"
        return formated_string
    
