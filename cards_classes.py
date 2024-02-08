from dataclasses import dataclass
from random import shuffle
from typing import List
import itertools


@dataclass
class Card:
    suit: str
    rank: str


@dataclass
class DeckOfCards:
    deck: List[Card]

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        # Create a deck of unique cards using the itertools method.
        self.deck = [Card(suit, rank) for suit, rank in itertools.product(suits, ranks)]

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_cards(self, num_cards):
        if num_cards <= len(self.deck):
            player_hand = self.deck[:num_cards]
            self.deck = self.deck[num_cards:]
            return player_hand
        else:
            print("Not enough cards in the deck.")
            return None
