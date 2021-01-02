#Get Players in hand:
def SetPlayers():
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
def SetDifficulty():
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