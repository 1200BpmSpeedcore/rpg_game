import json
import helper

# Liest die gesamte JSON-Datei.
# Inhalt ist so formatiert, dass "rooms" als Dictionary angelegt wird.
with open('files/rooms.json') as json_file:
    rooms = json.load(json_file)

monster = helper.addMonster(rooms)

currentRoom = 'Hall'
inventory = []

helper.showInstructions()

isEnd = False
while not isEnd:
    # Leerzeile, damit mehr Platz zwischen Ein- und Ausgabefenster ist.
    print()
    command = input('> ').lower().split()
    if len(command) == 0:
        print('Leere Eingabe!')
        continue

    if command[0] == 'help':
        helper.showCommands()
    elif command[0] == 'fight':
        isEnd = helper.handleFight(rooms, currentRoom, inventory, monster)
    elif command[0] == 'get':
        isEnd = helper.handleItemPickup(rooms, currentRoom, inventory, monster)
    elif command[0] == 'go':
        try:
            currentRoom = helper.showNewRoom(rooms, currentRoom, command[1], monster)
        except IndexError:
            helper.showInvalidCommand()
            continue
    elif command[0] == 'map':
        helper.showDirections(rooms, currentRoom)
    elif command[0] == 'status':
        helper.showStatus(rooms, currentRoom, inventory, monster)
    elif command[0] == 'exit':
        isEnd = True
    else:
        helper.showInvalidCommand()
    if not isEnd:
        isEnd = helper.showWinningScreenIfTrue(currentRoom, inventory)