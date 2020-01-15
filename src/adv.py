from room import Room
from player import Player
from item import Item

#Declare all the items

item = {
    'outside_item':  Item("outsideI",
                     "outside item description"),

    'foyer_item':    Item("foyerI", """foyer item description."""),

    'overlook_item': Item("overlookI", """overlook item description."""),

    'narrow_item':   Item("narrowI", """narrow item description."""),

    'treasure_item': Item("treasureI", """treasure item description."""),
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

def get_user_choice(choice):   
    
    if player.current_room.name == room["outside"].name and choice == "n":
        player.current_room = room["foyer"]  
        room.room_items = item["foyer_item"]     
    
    elif player.current_room.name == room["foyer"].name and choice == "s":
        player.current_room = room["outside"] 

    elif player.current_room.name == room["foyer"].name and choice == "n":
        player.current_room = room["overlook"] 

    elif player.current_room.name == room["foyer"].name and choice == "e":
        player.current_room = room["narrow"] 

    elif player.current_room.name == room["overlook"].name and choice == "s":
        player.current_room = room["foyer"] 

    elif player.current_room.name == room["narrow"].name and choice == "w":
        player.current_room = room["foyer"] 

    elif player.current_room.name == room["narrow"].name and choice == "n":
        player.current_room = room["treasure"] 

    elif player.current_room.name == room["treasure"].name and choice == "s":
        player.current_room = room["narrow"] 

    else:
        print("Ooops! There is nowhere out there...")       

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
#room_obj = Room(room["outside"].name, room["outside"].description)
#player = Player("Tom", room_obj.name, room_obj.description)

player = Player("Tom", room["outside"].name, room["outside"].description)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print()
while True:
    print("\t**********************************")
    print("\tTEXT ADVENTURE GAME")
    print("\t**********************************")
    print("You are in the %s" %(player.current_room))
    print("\tn >>> move to the north ")
    print("\ts >>> move to the south ")
    print("\te >>> move to the east ")
    print("\tw >>> move to the west ")
    print("\tq >>> Exit")
    user_choice = input(">>> ")#reads in the menu choice entered by the user

    if user_choice == "q":
        print("Thanks for Playing. Come again soon...")
        break
    else:
        get_user_choice(user_choice)
    