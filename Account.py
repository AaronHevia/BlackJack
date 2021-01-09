class Account:

    def __init__(self):
        pass

    def AddNewPlayer(self, activePlayers, name, pwd, pin, characters):
        # New players will start with $1000, $$ Won, $$ Lost, Ciphered Password, PIN, and Shuffled Alphabet    
        player  = activePlayers[name] = [1000, 0, 0, password, pin, characters]
        return player

    def NewPlayer(self, activePlayers, retiredPlayers):    
        allPlayers = activePlayers | retiredPlayers    
        name = input("\nEnter a player name:  ")        

        if len(allPlayers) == 0:        
            #TODO:  Password, PIN and Characters creation.
            pwd = ""    #TODO:  Get password from Password Class.
            pin = 0 #TODO: Get "PIN" (Cipher) from Password Class.
            # characters = password.Shuffle() 
        else:
            for player in allPlayers:
                if name == player:
                    print("Player already exists in session.  Enter a new player.")
                    self.NewPlayer(activePlayers, retiredPlayers)
                else:                
                    #TODO:  Password, PIN and Characters creation.
                    pwd = ""    #TODO:  Get password from Password Class.
                    pin = 0 #TODO: Get "PIN" (Cipher) from Password Class.
                    characters = [] #TODO: Get shuffled characters from Password Class.
            
        self.AddNewPlayer(activePlayers, name, password, pin, characters)
        return activePlayers

    def RetirePlayer(self, activePlayers, retiredPlayers):
        name = input("Which player will be retiring:  ")
        #TODO:  Validate account to retire.
        retiredPlayers[name] = activePlayers[name]    
        del activePlayers[name]
        print(f"{name} has retired with ${retiredPlayers[name][0]}.  You have made ${retiredPlayers[name][1]} and lost ${retiredPlayers[name][2]} in this session.")

    def UnretirePlayer(self, activePlayers, retiredPlayers):
        name = input("Which player will be returning to the table:  ")
        #TODO:  Validate account to return.
        activePlayers[name] = retiredPlayers[name]
        del retiredPlayers[name]
        print(f"Welcome back {name}.  You have ${activePlayers[name][0]} remaining.  Good luck!")