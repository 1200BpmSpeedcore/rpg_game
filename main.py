import json
import output_helper

with open('files/rooms.json') as json_file:
    rooms = json.load(json_file)

currentRoom = 'Hall'
inventory = []

output_helper.showInstructions()

end = False
while not end:
    print()
    command = input('> ').lower().split()
    if command[0] == 'help':
        output_helper.showCommands()
    elif command[0] == 'get':
        end = output_helper.handleItemPickup(rooms, currentRoom, inventory)
    elif command[0] == 'go':
        try:
            currentRoom = output_helper.showNewRoom(rooms, currentRoom, command[1])
        except IndexError:
            output_helper.showInvalidCommand()
            continue
        end = output_helper.showWinningScreenIfTrue(currentRoom, inventory)
    elif command[0] == 'map':
        output_helper.showDirections(rooms, currentRoom)
    elif command[0] == 'status':
        output_helper.showStatus(rooms, currentRoom, inventory)
    elif command[0] == 'exit':
        end = True
    else:
        output_helper.showInvalidCommand()