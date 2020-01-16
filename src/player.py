# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    #current_room points to Room class 
    def __init__(self, name, player_room_name, player_room_description, player_inventoy = []): 
        self.name = name
        self.current_room = Room(player_room_name, player_room_description)
        self.player_inventory = []

    def add_item(self, found_item):
        self.player_inventory.append(found_item)

    def drop_item(self, found_item_index):
        del self.player_inventory[found_item_index]




