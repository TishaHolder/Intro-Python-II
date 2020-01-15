# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, player_room_name, player_room_description): #current_room points to name in the Room class 
        self.name = name
        self.current_room = Room(player_room_name, player_room_description)

