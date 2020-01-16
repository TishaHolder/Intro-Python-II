# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    """The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that 
       respective direction."""
    def __init__(self, name, description, room_items = []):
        self.name = name 
        self.description = description
        self.room_items = room_items    

        #None is used to declare an attribute in Python without a value
        #The None keyword is used to define a null variable
        #can overwrite None in a class method
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None    

    def add_item(self, found_item):
        self.room_items.append(found_item)

    def on_take(found_item):
        print("You picked up %s" %(found_item))

    def remove_item(self, found_item_index):
        del self.room_items[found_item_index]

    def on_drop(dropped_item):
        print("You dropped %s" %(dropped_item))

    def __str__(self):
        return self.name + ': ' + self.description




