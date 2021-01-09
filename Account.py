class Account:

    def __init__(self):
        self.password = ""    # TODO:  Get password from Password Class.
        self.pin = 0 # TODO: Get "PIN" (Cipher) from Password Class.
        self.characters = [] # TODO: Get shuffled characters from Password Class.


    def get_password(self):
        # TODO:  Password, PIN and Characters creation:
        pass
        
        
    def new_player(self, activePlayers, retiredPlayers):
        # Merge lists of dictionaries to conduct only 1 parse.            
        allPlayers = activePlayers | retiredPlayers    
        name = input("\nEnter a player name:  ")        

        if len(allPlayers) == 0:        
            self.get_password()
        else:
            for player in allPlayers:
                if name == player:
                    print("Player already exists in session.  Enter a new player.")
                    self.new_player(activePlayers, retiredPlayers)
                else:                
                    self.get_password

        # New players will start with $1000, $$ Won, $$ Lost, Ciphered Password, PIN, and Shuffled Alphabet            
        activePlayers[name] = [1000, 0, 0, self.password, self.pin, self.characters] 
        #clear password, pin and characters to protect info.
        self.password = ""
        self.pin = 0
        self.characters = []
        
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