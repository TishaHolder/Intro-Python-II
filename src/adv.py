from room import Room
from player import Player
from item import Item
from item import Umbrella
from item import FlashLight
from item import Binoculars
from item import Directions
from item import Chest
from item import Pillow
from item import Sword
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
earlier adventurers. Exit to the south or go north to slay the dragon."""),    

    'dungeon': Room("Dungeon", """You might need a sword to slay the dragon. If you make it out alive,
go south and get some much needed rest in the bedroom."""),

'bedroom': Room("Bedroom", """I see you defeated the dragon. Now you can rest. When you are ready to start exploring again,
you can exit to the south."""),


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
room['treasure'].n_to = room['dungeon']
room['dungeon'].s_to = room['bedroom']
room['bedroom'].s_to = room['overlook']

#Declare all the room items
umbrella = Umbrella("umbrella", "protect yourself from the elements", "large")
flashlight = FlashLight("flashlight", """you might need this to see better.""", "very bright")
binoculars = Binoculars("binoculars", """see the scenic views from the overlook.""", "100")
directions = Directions("directions", """you will need this if you get lost.""", "portrait")
chest = Chest("chest", """collect your treasures.""", "empty") 
pillow = Pillow("pillow", """the bed is made of brass, you might need this to sleep better.""", "medium")
sword = Sword("sword", """use this if you can't slay the dragon with your bare hands.""", "very sharp" )

outside_items = [umbrella.name, flashlight.name, directions.name]
foyer_items = [umbrella.name, flashlight.name, binoculars.name]
overlook_items = [binoculars.name, flashlight.name, chest.name]
narrow_items = [directions.name, flashlight.name]
treasure_items = [chest.name, flashlight.name]
bedroom_items = [pillow.name, flashlight.name, chest.name, directions.name]
dungeon_items = [sword.name, flashlight.name, directions.name]

# Add items to rooms
room['outside'].room_items = outside_items
room['foyer'].room_items = foyer_items
room['overlook'].room_items = overlook_items
room['narrow'].room_items = narrow_items
room['treasure'].room_items = treasure_items
room['bedroom'].room_items = bedroom_items
room['dungeon'].room_items = dungeon_items

#Declare all player inventory items
snacks = Food("snacks", "you might get the munchies", 100)
water = Water("water", """this is going to be a long day, stay hydrated.""", "spring")

#process the 4 directions
def process_directions(choice):
    if choice == "i":        
       print("Your inventory items: %s" %(player.player_inventory))

    else:

        if player.current_room.name == room["outside"].name and choice == "n":      
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

        elif player.current_room.name == room["treasure"].name and choice == "n":
            player.current_room = room['treasure'].n_to        
            player.current_room.room_items = room['dungeon'].room_items 

        elif player.current_room.name == room["dungeon"].name and choice == "s":
            player.current_room = room['dungeon'].s_to        
            player.current_room.room_items = room['bedroom'].room_items 

        elif player.current_room.name == room["bedroom"].name and choice == "s":
            player.current_room = room['bedroom'].s_to        
            player.current_room.room_items = room['overlook'].room_items 

        else:
            print("Ooops! There is nowhere out there...")  

def process_user_request(parsed_entry):
    get_word = "get"
    take_word = "take"
    drop_word = "drop"
    found_item_index = -1
    found_item = None        

    if get_word in parsed_entry or take_word in parsed_entry:
        #index method returns the index of where the item is in the list
        #it returns a ValueError if it is not found. the if statement at the end of the line prevents the value error
        found_item_index = player.current_room.room_items.index(parsed_entry[1]) if parsed_entry[1] in player.current_room.room_items else -1
        if found_item_index >= 0:
            found_item = player.current_room.room_items[found_item_index]
            player.current_room.remove_item(found_item_index)
            player.current_room.on_take(found_item)
            player.add_item(found_item)                
        else:
            print("I am sorry, that item is not available in this room.")

    elif drop_word in parsed_entry:
        #index method returns the index of where the item is in the list
        #it returns a ValueError if it is not found. the if statement at the end of the line prevents the value error
        found_item_index = player.player_inventory.index(parsed_entry[1]) if parsed_entry[1] in player.player_inventory else -1
        if found_item_index >= 0:
            found_item = player.player_inventory[found_item_index]
            player.current_room.add_item(found_item)
            player.current_room.on_drop(found_item)
            player.drop_item(found_item_index)
        else:
            print("I am sorry, that item is not in your inventory.")

    else:
        print("I am sorry. We did not understand your request. Please try your request again.") 


#processes the user's menu entry
def parser(choice):
    parsed_entry = choice.split()
    verb = False
    verb_object = False    

    if len(parsed_entry) == 1:
        verb = True
        process_directions(choice)
        return verb
    elif len(parsed_entry) == 2:
        verb_object = True
        process_user_request(parsed_entry)
        return verb_object
    else:
        print("I am sorry. We did not understand your request. Please try your request again.")     


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Add items to player inventory

player = Player("Tom", room["outside"].name, room["outside"].description)
player.current_room.room_items = room["outside"].room_items
player.player_inventory = [snacks.name, water.name]


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
    print('You are in the %s \nYou can "get" or "take" any of these items >> %s' %(player.current_room, player.current_room.room_items))
    print("\ti >>> view your inventory ")
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
        parser(user_choice)
        #get_user_choice(user_choice)
    