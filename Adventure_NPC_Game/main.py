

# this is the main of the program

from adventure_npc_game import Game
from adventure_npc_game import Room
from adventure_npc_game import Item, NPC

r = Room("Detective's Office", "You are in a cluttered office filled with case files and dim lighting.", m_item=Item("Notebook", "You see a worn notebook filled with scriblled notes and observations.", 0.5),
          m_npc=NPC("Inspector Graves", "Look closely detective. The smallest detail may lead to the biggest revealation.")
         , adjacent_rooms={'south':'Dark Alley', 'east':'City Hall'})

g = Game(r)
g.play()