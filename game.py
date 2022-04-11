#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

from audioop import add
from webbrowser import get


def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'north': 'Apothecary',
        'west': 'Dark Bedroom',
        'item': 'bronze-key'
    },
    'Kitchen': {
        'north': 'Hall',
        'south': 'Closet',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'vanilla-extract',
        'north': 'Pantry',
    },
    'Garden': {
        'north': 'Dining Room',
        'item': 'gold-extract',
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'mercury-extract',
    },
    'Apothecary': {
        'south': 'Hall',
        'item': 'stoneskin-extract',
    },
    'Closet': {
        'north': 'Kitchen',
        'item': 'silver-key'
    },
    'Dark Bedroom': {
        'east': 'Hall',
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # Define how a player can win
    if currentRoom == 'Garden' and 'bronze-key' in inventory and 'silver-key' in inventory and 'gold-key' in inventory:
        print('Using the 3 keys you found you escaped the house safely')
        break

    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'stoneskin-extract' in inventory:
            print(
                'A monster charges you, your stonskin-extract stops the moster in its tracks and knocks it out')
        else:
            print('A monster tramples you, you die. GAME OVER')
            break

    if currentRoom == 'Dark Bedroom' and 'gold-extract' in inventory:
        print('Your gold-extract detects a gold-key under the floorboard, you take it')
        inventory.append('gold-key')
    elif currentRoom == 'Dark Bedroom':
        print('You dont see anything of interest in here')
