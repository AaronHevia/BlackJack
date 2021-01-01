cardList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suitList = ["Spades", "Diamonds", "Hearts", "Clubs"]

suitDictionary = {
    "Spades": "♠", 
    "Diamonds": "♦", 
    "Hearts": "♥", 
    "Clubs": "♣"
}

cardValues = {
    "A": 11,    
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

#Create a 52 card deck:
def BuildDeck():    
    deck = []

    for card in cardList:    
        for suit in suitList:
            tempList = [card, suit]
            deck.append(tempList)
    
    return deck

#ASCII image of a drawn card:
def DrawCard(card, suit):
    icon = suitDictionary[suit]
    cardPos1 = ""
    cardPos2 = ""

    if card == "10":
        cardPos1 = "1"
        cardPos2 = "0"
    else:
        cardPos1 = card
    
    drawnCard = [
        "┌─────┐",
        f"|{cardPos1}{cardPos2}   |",
        "|     |",
        f"|  {icon}  |",
        "|     |",
        f"|   {cardPos1}{cardPos2}|",
        "└─────┘"
    ]
    
    return drawnCard

#ASCII image of a Face-Down Card:
def DrawFaceDown():
    faceDown = [
        "┌─────┐", 
        "|░░░░░|",
        "|░░░░░|",
        "|░░░░░|",
        "|░░░░░|",
        "|░░░░░|",
        "└─────┘"
    ]
    return faceDown