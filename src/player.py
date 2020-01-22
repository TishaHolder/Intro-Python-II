# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    #you never want to pass mutable datatypes such as a lists or dictionaries as default arguments 
    #eg: player_inventory = []
    #instead use player_inventory = None and use an if/else check to see if the argument is provided (see below)
    def __init__(self, name, current_room, player_inventory = None): 
        self.name = name
        self.current_room = current_room
    
        if player_inventory is None:
            self.player_inventory = []
        else:        
            self.player_inventory = player_inventory

    def display_inventory(self):
        if self.player_inventory is None:
            print("There are no items in your inventory...")
        else:
            print("The items in your inventory are: ")
            for item in self.player_inventory:
                print(item)
    
    def move_player(self, direction):   
        if direction == "n" and self.current_room.n_to is not None:
           self.current_room = self.current_room.n_to           
        elif direction == "s" and self.current_room.s_to is not None:
            self.current_room = self.current_room.s_to           
        elif direction == "e" and self.current_room.e_to is not None:
            self.current_room = self.current_room.e_to            
        elif direction == "w" and self.current_room.w_to is not None:
            self.current_room = self.current_room.w_to 
        else:
            print("Ooops! There is nowhere out there...")            

    def display_room(self):       
        print("You are in the %s" %(self.current_room))
        if self.current_room.room_items is None:
            print("There are no items in this room.")
        else:
            print("The item(s) in this room: ")
            for item in self.current_room.room_items:
                print(item)

    def add_item(self, found_item):
        self.player_inventory.append(found_item)

    def drop_item(self, found_item_index):
        del self.player_inventory[found_item_index]    
        

    


