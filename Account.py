import Password

def AddNewPlayer(activePlayers, name, password, pin, characters):
    # New players will start with $1000, $$ Won, $$ Lost, Ciphered Password, PIN, and Shuffled Alphabet    
    player  = activePlayers[name] = [1000, 0, 0, password, pin, characters]
    return player

def NewPlayer(activePlayers, retiredPlayers):    
    allPlayers = activePlayers | retiredPlayers    
    name = input("\nEnter a player name:  ")
    i = len(allPlayers)

    if i == 0:
        print("Need to create Password and PIN.")
        #TODO:  Password, PIN and Characters creation.
        password = ""    #TODO:  Get password from Password Class.
        pin = 0 #TODO: Get "PIN" (Cipher) from Password Class.
        characters = [] #TODO: Get shuffled characters from Password Class.
    else:
        for player in allPlayers:
            if name == player:
                print("Player already exists in session.  Enter a new player.")
                NewPlayer(activePlayers, retiredPlayers)
            else:
                print("Need to create Password and PIN.")
                #TODO:  Password, PIN and Characters creation.
                password = ""    #TODO:  Get password from Password Class.
                pin = 0 #TODO: Get "PIN" (Cipher) from Password Class.
                characters = [] #TODO: Get shuffled characters from Password Class.
        
    AddNewPlayer(activePlayers, name, password, pin, characters)
    return activePlayers

def RetirePlayer(activePlayers, retiredPlayers):
    name = input("Which player will be retiring:  ")
    #TODO:  Validate account to retire.
    retiredPlayers[name] = activePlayers[name]    
    del activePlayers[name]
    print(f"{name} has retired with ${retiredPlayers[name][0]}.  You have made ${retiredPlayers[name][1]} and lost ${retiredPlayers[name][2]} in this session.")

def UnretirePlayer(activePlayers, retiredPlayers):
    name = input("Which player will be returning to the table:  ")
    #TODO:  Validate account to return.
    activePlayers[name] = retiredPlayers[name]
    del retiredPlayers[name]
    print(f"Welcome back {name}.  You have ${activePlayers[name][0]} remaining.  Good luck!")