import random

POSSIBLE_SUITS = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

POSSIBLE_VALUES = range(1,14)

VALUES_MAP = {
    1: 'A',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'J',
    12: 'Q',
    13: 'K',
}

SUITS_MAP = {
    'Hearts': '♡',
    'Spades': '♤',
    'Diamonds': '♢',
    'Clubs': '♧',
}

class Card:
    def __init__(self, suit, value, face_up=False, location="Deck"):
        self.suit = suit
        self.value = value
        self.face_up = face_up
        self.location = location

    def __repr__(self):
        return f"{VALUES_MAP[self.value]}{SUITS_MAP[self.suit]}"

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

    def get_top_card(self):
        return self.cards.pop(0)
    
    def __repr__(self):
       return f"a Deck of {len(self.cards)} cards."
    
class Game:
    def __init__(self, rows=3, columns=4):
        self.game_deck = Deck()
        self.game_deck.shuffle()
        self.game_board = []
        for row in range(rows):
            self.game_board.append([])
            for column in range(columns):
                self.game_board[row].append(self.game_deck.cards.pop(0))

    # need to display top card face up
    # need to get player input on where to place top card next
        # add top card to player's chosen location, on top of "stack"

