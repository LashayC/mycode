#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('"
    RPG Game
    =======
    Commands:
        go [direction]
        get [item]
    "')

def showStatus():
    """determine the current status of player"""
    #print the players current location
    print('---------------------------')
    print('You are in the ' + currentRoom)

    # print what player is carrying
    print('Inventory:', inventory)

    # check if there's an item in the room, if so, print it
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

def main():

    # an inventory which is initally empty
    inventory = []

    # a dictionary linking a room to other rooms
    rooms = {
                'Hall': {
                    'south' : 'Kitchen'
                    },
                
                'Kitchen' : {
                    'north' : 'Hall'
                    }
            }

    #start the player in the Hall
    currentRoom = 'Hall'

    # breaking this while loop means the game is over
    while True:
        showStatus()

        #the player MUST type something in
        #otherwise input will keep asking
        move = ''
        while move == '':
            move = input('>')

        #normalizing input:
        # .lower() makes lowercase, .split() creates list
        # "get golden key" becomes ["get", "golden key"]
        move = move.lower().split(" ", 1)

        #if they type 'go' first
        if move[0] == 'go':
            # check that they are allowed to go wherever they want to go
            if move[1] in rooms[currentRoom]:
                #set current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            #if they are'nt allowed to go that way:
            else:
                print('You can\'t go that way!')

        #if they type 'get' first
        if move[0] == 'get' :
            # make 2 checks
            # 1 if current room contains item
            # 2 if the item in the room matches the item the player wishes to get
            if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                    # add item to inventory
                    inventory.append(move[1])
                    #display helpful message
                print(move[1] + ' got!')
                # delete the item key:value pair from rooms dictionary
                del rooms[currentRoom]['item']
                



if __name__ == "__main__":
    main()
