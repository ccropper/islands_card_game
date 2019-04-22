import random

POSSIBLE_SUITS = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

POSSIBLE_VALUES = range(1,14)

VALUES_MAP = {
    1: 'Ace',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Jack',
    12: 'Queen',
    13: 'King',
}

class Card:
    def __init__(self, suit, value, face_up=False, location="Deck"):
        self.suit = suit
        self.value = value
        self.face_up = face_up
        self.location = location

    def __repr__(self):
        return f"{VALUES_MAP[self.value]} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for suit in POSSIBLE_SUITS:
            for value in POSSIBLE_VALUES:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def __repr__(self):
       return f"a Deck of {len(self.cards)} cards."
    
