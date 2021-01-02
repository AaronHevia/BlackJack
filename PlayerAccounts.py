# Add New Player

# Password

def NewPlayer(dictionary1, dictionary2):   
    allPlayers = dictionary1 | dictionary2

    def AddNewPlayer(name):
        player  = dictionary1[name] = 1000
        return player
    
    name = input("\nEnter a player name:  ")
    i = len(allPlayers)

    if i == 0:
        AddNewPlayer(name)
    else:
        for player in allPlayers:            
            if name == player:
                print("Player already exists in session.  Enter a new player.")
                NewPlayer(dictionary1, dictionary2)
            else:
                AddNewPlayer(name)
        
    return dictionary1



# Retire Player

# Unretire Player