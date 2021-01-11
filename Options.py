from validator import Validator

VALIDATOR = Validator()

class Options:    
    
    #Get Players in hand:
    def set_players(self):
        """Sets the number of players that will be playing in the following hand."""
        while True:
            players = input("\nHow many people will be playing this hand? Choose a number from 1-7:  ")
            try:
                val = int(players)
                if val > 0 and val < 8:
                    break
                else:
                    print("Invalid amount.  Try again.")
            except ValueError:
                print("The number of players must be from 1 to 7.  Try again.")
        return val

    #Difficulty: 1-9
    def set_difficulty(self):
        """Raises difficulty of the game.  The higher the number, the more decks that will be used (Difficulty will be 2 levels higher than the amount of players playing when there are 2 or more players)."""
        #TODO:  Fix logic so that it will automatically add or drop decks as players come in and out of the game.
        while True:
            difficulty = input("\nChoose level of difficulty from 1-9:  ")
            try:
                val = int(difficulty)
                if val > 0 and val < 10:
                    break
                else:
                    print("Invalid difficulty.  Try again.")
            except ValueError:
                print("Difficulty must be a number from 1 to 9.  Try again.")
        return val