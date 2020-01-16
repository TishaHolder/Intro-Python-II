from room import Room
from player import Player
from item import Item
from item import Umbrella
from item import FlashLight
from item import Binoculars
from item import Directions
from item import Chest
from item import Food
from item import Water


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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

#Declare all the room items

umbrella = Umbrella("umbrella", "protect yourself from the elements", "large")

flashlight = FlashLight("flashlight", """you might need this to see better.""", "very bright")

binoculars = Binoculars("binoculars", """see the scenic views from the overlook.""", "100")

directions = Directions("directions", """you will need this if you get lost.""", "portrait")

chest = Chest("chest", """collect your treasures.""", "empty") 

outside_items = [umbrella]
foyer_items = [flashlight]
overlook_items = [binoculars]
narrow_items = [directions]
treasure_items = [chest]

# Add items to rooms
room['outside'].room_items = outside_items
room['foyer'].room_items = foyer_items
room['overlook'].room_items = overlook_items
room['narrow'].room_items = narrow_items
room['treasure'].room_items = treasure_items

#Declare all player inventory items
snacks = Food("snacks", "you might get the munchies", 100)
water = FlashLight("water", """this is going to be a long day, stay hydrated.""", "spring")


def get_user_choice(choice):   
    
    if player.current_room.name == room["outside"].name and choice == "n":
       #player.current_room = room["foyer"]  
        #room.room_items = item["foyer_item"] 
        player.current_room = room['outside'].n_to        
        player.current_room.room_items = room['foyer'].room_items
    
    elif player.current_room.name == room["foyer"].name and choice == "s":
        player.current_room = room['foyer'].s_to        
        player.current_room.room_items = room['outside'].room_items

    elif player.current_room.name == room["foyer"].name and choice == "n":
        player.current_room = room['foyer'].n_to        
        player.current_room.room_items = room['overlook'].room_items 

    elif player.current_room.name == room["foyer"].name and choice == "e":
         player.current_room = room['foyer'].e_to        
         player.current_room.room_items = room['narrow'].room_items 

    elif player.current_room.name == room["overlook"].name and choice == "s":
         player.current_room = room['overlook'].s_to        
         player.current_room.room_items = room['foyer'].room_items 

    elif player.current_room.name == room["narrow"].name and choice == "w":
         player.current_room = room['narrow'].w_to        
         player.current_room.room_items = room['foyer'].room_items 

    elif player.current_room.name == room["narrow"].name and choice == "n":
         player.current_room = room['narrow'].n_to        
         player.current_room.room_items = room['treasure'].room_items 

    elif player.current_room.name == room["treasure"].name and choice == "s":
         player.current_room = room['treasure'].s_to        
         player.current_room.room_items = room['narrow'].room_items 

    else:
        print("Ooops! There is nowhere out there...")       

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Add items to player inventory

player = Player("Tom", room["outside"].name, room["outside"].description)
player.current_room.room_items = room["outside"].room_items
player.player_inventory = [snacks, water]


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
    print("You are in the %s To see here>> %s" %(player.current_room, player.current_room.room_items))
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
    