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
    #Merge dictionaries to make a single search.
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



# Retire Player
    #Copy active player account info to retiredPlayers
    #Delete copied active player account in activePlayers

# Unretire Player
    #Copy retired player account info to activePlayers
    #Delete copied retired player account in retiredPlayers