import random
import time

# Fügt einem zufälligen Raum ein zufälliges Monster in dem Dictionary "rooms" hinzu.
# Gibt den Namen des Monsters zurück
def addMonster(rooms):
    possibleMonster = ['dragon', 'psyclops', 'minotaurus']
    monster = possibleMonster[random.randint(0, len(possibleMonster) - 1)]

    roomKeys = list(rooms.keys())
    room = roomKeys[random.randint(0, len(roomKeys) - 1)]

    rooms[room]["monster"] = monster
    return monster

def showInstructions():
    print('''
Welcome to your own RPG Game
============================

Get to the Garden with a key and a potion
or get to the Laboratory with a BookOfLife and a Beam-O-Mat.

Avoid the monster or fight it (if you are brave enough).

Type 'help' for commands
============================''')

def showCommands():
    print('''Commands:
    fight
    get
    go [direction]
    map
    status

    exit''')

# Beginnt einen Kampf, wenn sich ein Monster im Raum befindet.
def handleFight(rooms, currentRoom, inventory, monsterName):
    if 'monster' not in rooms[currentRoom]:
        print('Your knuckles were ready but there was monster in this room')
        print('waiting for you')
        return False
    print('Your rapid charge awoke the', monsterName + '.')
    print('You stopped and got ready for its attack.')
    return startFight(rooms, currentRoom, inventory, monsterName)

# Gibt booleaschen Wert zurück, ob der Kampf gegen das Monster VERLOREN wurde.
def startFight(rooms, currentRoom, inventory, monsterName):
    if 'chainsaw' in inventory:
        inventory.remove('chainsaw')
        if 'bottle of olive oil' in inventory:
            print('You used your chainsaw and olive oil to defend yourself, killing')
            print('the', monsterName, 'in the process.')
            inventory.remove('bottle of olive oil')

            # Lässt die Konsole für 3 Sekunden einfrieren
            time.sleep(3)
            print()
            print('OH!')
            print('The', monsterName, 'dropped a key!')
            del rooms[currentRoom]['monster']
            inventory.append('key')
            return False
        else:
            print("You tried to defend yourself by using your chainsaw. The engine didn't")
            print('start running because the saw was out of gas. With an unuseable weapon')
            print("you didn't stand a chance against the", monsterName + '!')
            print('YOU DIED ¯\\_(ツ)_/¯')
            return True
    else:
        print("You didn't have any weapon to defend yourself.")
        print('YOU DIED ¯\\_(ツ)_/¯')
        return True

# Hebt Item im Raum auf, wenn vorhanden.
# Wenn sich das Monster im Raum befindet startet ein Kampf.
def handleItemPickup(rooms, currentRoom, inventory, monsterName):
    item = ''
    try:
        item = rooms[currentRoom]['item']
    except:
        pass

    isDead = False
    if item == '':
        print('There is no item in this room')

    if item == '' and 'monster' in rooms[currentRoom]:
        print('The', monsterName, 'has awaken attacking you.')

        isDead = startFight(rooms, currentRoom, inventory, monsterName)
    elif item != '' and 'monster' in rooms[currentRoom]:
        print('You tried to pick up a', item , 'but the', monsterName, 'has awaken')
        print('attacking you.')

        isDead = startFight(rooms, currentRoom, inventory, monsterName)
    else:
        inventory.append(item)
        print('You added a', item, 'to your inventory')
        if item == 'chainsaw':
            print('Groovy!')
        del rooms[currentRoom]['item']
    return isDead

def showNewRoom(rooms, currentRoom, direction, monsterName):
    currentRoomOld = currentRoom
    try:
        currentRoom = rooms[currentRoom][direction]
    except:
        print("You can't go this way")
        return currentRoom

    if 'monster' in rooms[currentRoomOld]:
        print('You sneaked around the sleeping', monsterName, 'and went to the', currentRoom + '.')
    else:
        print('You went to the', currentRoom)

    if 'monster' in rooms[currentRoom]:
        print('This room has a sleeping', monsterName, 'in it.')
    return currentRoom

def showInvalidCommand():
    print('''Invalid Input!
Type 'help' for commands.''')

def showDirections(rooms, currentRoom):
    for direction, neighbour in rooms[currentRoom].items():
        if direction in ['north', 'east', 'south', 'west']:
            print(direction, "\t ->", neighbour)

def showStatus(rooms, currentRoom, inventory, monsterName):
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
    # monster in current room
    if 'monster' in rooms[currentRoom]:
        print('This room has a sleeping', monsterName, 'in it.')
    print("---------------------------")

# So struktriert, dass die Funktion, um potentiell weitere Siegbedingungen erweitert werden kann.
def showWinningScreenIfTrue(room, inventory):
    won = room == 'Garden' and 'key' in inventory and 'potion' in inventory
    won = won or (room == 'Laboratory' and 'BookOfLife' in inventory and 'Beam-O-Mat' in inventory)
    if won:
        print('============================')
        print('CONGRATULATIONS!')
        print('You escaped the dungeon!')
        print('============================')
    return won