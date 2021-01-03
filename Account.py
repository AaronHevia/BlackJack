import Password

# TODO: Get shuffled alphabet. from Password Class.

# TODO: Get "PIN" (Cipher) from Password Class.

# Add New Player
def AddNewPlayer(activePlayers, name):
    # New players will start with $1000, $$ Won, $$ Lost, Ciphered Password, PIN, and Shuffled Alphabet
    pwd = ""
    pin = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    player  = activePlayers[name] = [1000, 0, 0, pwd, pin, alphabet]
    return player

def NewPlayer(activePlayers, retiredPlayers):    
    allPlayers = activePlayers | retiredPlayers    
    name = input("\nEnter a player name:  ")
    i = len(allPlayers)

    if i == 0:
        AddNewPlayer(activePlayers, name)
    else:
        for player in allPlayers:            
            if name == player:
                print("Player already exists in session.  Enter a new player.")
                NewPlayer(activePlayers, retiredPlayers)
            else:
                AddNewPlayer(activePlayers, name)
        
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