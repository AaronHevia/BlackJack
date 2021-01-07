class Card:

    def __init__(self):
        self.card_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.suit_list = ["Spades", "Diamonds", "Hearts", "Clubs"]

        self.suits = {
            "Spades": "♠", 
            "Diamonds": "♦", 
            "Hearts": "♥", 
            "Clubs": "♣"
        }

        self.card_values = {
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

    
    def build_deck(self):
        """Builds a deck depending on difficulty level."""

        deck = []

        for card in self.card_list:    
            for suit in self.suit_list:
                temp_list = [card, suit]
                deck.append(temp_list)    
        return deck


    def draw_card(self, card, suit):
        """Creates an ASCII image of the drawn card."""

        icon = self.suits[suit]
        card_digit_1 = ""
        card_digit_2 = ""

        if card == "10":
            card_digit_1 = "1"
            card_digit_2 = "0"
        else:
            card_digit_1 = card
    
        drawn_card = [
            "┌─────┐",
            f"|{card_digit_1}{card_digit_2}   |",
            "|     |",
            f"|  {icon}  |",
            "|     |",
            f"|   {card_digit_1}{card_digit_2}|",
            "└─────┘"
        ]    
        return drawn_card
    

    def draw_face_down(self):
        """Creates an ASCII image of a face-down card."""
        
        face_down = [
            "┌─────┐", 
            "|░░░░░|",
            "|░░░░░|",
            "|░░░░░|",
            "|░░░░░|",
            "|░░░░░|",
            "└─────┘"
        ]
        return face_down