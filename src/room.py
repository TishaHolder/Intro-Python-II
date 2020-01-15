# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    """The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that 
       respective direction."""
    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.room_items = []    

        #None is used to declare an attribute in Python without a value
        #can overwrite None in a class method
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return self.name + ': ' + self.description




