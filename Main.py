import os
import sys
import random
import Options
import Account
import Cards
from Art import logo

activePlayers = {}
retiredPlayers = {}

deck = Cards.BuildDeck()
gameDeck = []
drawFaceDown = Cards.DrawFaceDown()
drawIndex = 0
drawCard = Cards.DrawCard("10", "Spades") #remove after testing

os.system('cls') #Remove after finished.  Arrange what to display and use in between each hand call.
print(logo)
players = Options.SetPlayers()
difficulty = Options.SetDifficulty()
for i in range(players):
    activePlayers = Account.NewPlayer(activePlayers, retiredPlayers)

# Used for troubleshooting account process:
print("Printing Live Players:\n")
for player in activePlayers:
    print(player)

print("Printing Old Players:\n")
for player in retiredPlayers:
    print(player)



# livePlayers = Options.EnterNewPlayer("Aaron")
# for player in livePlayers:
#     print(f"{player} has ${livePlayers[player]}.")



# print(deck[0])
# random.shuffle(deck)
# print(deck[0])
# print(len(deck))
# del deck[0]
# print(deck[0])
# print(len(deck))

# for line in drawCard:
#     print(f"{drawCard[drawIndex]}  {drawFaceDown[drawIndex]}")
#     drawIndex +=1


# print(logo)
# print(len(deck))






#How many players?

#Enter Bids
    #min 5.00

#TODO:  Shuffle

#TODO:  Deal to players

#TODO:  Deal to Dealer

#TODO:  Deal to players

#TODO:  Deal to Dealer Face Down

#TODO:  Split Pairs

#TODO:  Winning bets:
#   Natural: Blackjack on dealt cards = 1.5 * bet
#    
#   Double down option:  If players add up to 9, 10, or 11 on dealt hand then are only given 1 card after.
#    
#   Insurance:  When the dealer's face-up card is an ace, any of the players may make a side bet of up to half the original bet that the dealer's face-down card is a ten-card,
# and thus a blackjack for the house. Once all such side bets are placed, the dealer looks at the hole card. If it is a ten-card,
# it is turned up, and those players who have made the insurance bet win and are paid double the amount of their half-bet - a 2 to 1 payoff. 