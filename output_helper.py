def showInstructions():
    print('''
Welcome to your own RPG Game
============================

Get to the Garden with a key and a potion.
Avoid the monsters!

Type 'help' for commands
============================''')

def showCommands():
    print('''Commands:
    get
    go [direction]
    map
    status

    exit''')

def showInvalidCommand():
    print('''Invalid Input!
Type 'help' for commands.''')

def showStatus(rooms, currentRoom, inventory):
    print('---------------------------')
    # current room
    print('You are in the ' + currentRoom)
    # inventory
    print('Inventory: ')
    if len(inventory) == 0:
        print("\tEmpty")
    else:
        for item in inventory:
            print("\t", item)
    # item in current room
    try:
        item = rooms[currentRoom]['item']
        print('You see a ' + item)
    except:
        pass
    print("---------------------------")

def showDirections(rooms, currentRoom):
    for direction, neighbour in rooms[currentRoom].items():
        if direction in ['north', 'east', 'south', 'west']:
            print(direction, "\t ->", neighbour)

def handleItemPickup(rooms, currentRoom, inventory):
    try:
        item = rooms[currentRoom]['item']
    except:
        print('There was no item in this room')
        return False
    if item == "monster":
        print('You tried to pick up a monster.')
        print('YOU DIED ¯\_(ツ)_/¯')
        return True
    elif item in inventory:
        print('You already got a', item)
    else:
        inventory.append(item)
        print('You added a', item, 'to your inventory')
        del rooms[currentRoom]['item']
    return False

def showNewRoom(rooms, currentRoom, direction):
    try:
        currentRoom = rooms[currentRoom][direction]
    except:
        print("You can't go this way")
        return currentRoom
    print('You went to the', currentRoom)
    return currentRoom

def showWinningScreenIfTrue(room, inventory):
    if room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('============================')
        print('CONGRATULATIONS')
        print('You escaped the dungeon')
        print('============================')
        return True
    return False