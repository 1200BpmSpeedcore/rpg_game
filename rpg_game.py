inventory = []
#a dictionary linking a room to other rooms
rooms = {
            'Hall' : { 'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
        'Kitchen' : { 'north' : 'Hall',
                'item' : 'monster'
            },
        'Dining Room' : { 'west' : 'Hall',
            'south' : 'Garden',
            'item' : 'potion'
            },
        'Garden' : { 'north' : 'Dining Room' }
    }
currentRoom = 'Hall'
inventory = ["Compass", "Water Pistol", "Chopsticks", 84, 3.2]
move = ''

def showInstructions():
    print('''
Welcome to your own RPG Game
============================

Get to the Garden with a key and a potion.
Avoid the monsters!

Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

def move1():
    global move
    while move == '':
        move = input('>')
    move = move.lower().split()

def move2():
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house... YOU WIN!')

showInstructions()
showStatus()
move1()
move2()