from dataclasses import dataclass
from random import shuffle
from typing import List
import itertools


@dataclass
class Card:
    """
        Represents a playing card with a suit and a rank.

        Attributes:
        - suit (str): The suit of the card (e.g., Hearts, Diamonds, Clubs, Spades).
        - rank (str): The rank of the card (e.g., 2, 3, Jack, Ace).
    """
    suit: str
    rank: str


@dataclass
class DeckOfCards:
    """
        Represents a deck of playing cards.

        Attributes:
        - deck (List[Card]): A list containing Card objects representing the deck.

        Methods:
        - __init__(): Initializes a new deck of cards with all possible combinations of suits and ranks.
        - shuffle_deck(): Shuffles the order of cards in the deck.
        - deal_cards(num_cards: int) -> List[Card] or None: Deals a specified number of cards from the deck.
    """
    deck: List[Card]

    def __init__(self):
        """
                Initialize a new deck of cards.

                Creates a deck with all possible combinations of suits and ranks.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        # Create a deck of unique cards using the itertools method.
        self.deck = [Card(suit, rank) for suit, rank in itertools.product(suits, ranks)]

    def shuffle_deck(self):
        """
                Shuffle the order of cards in the deck.

                Uses the random.shuffle function to shuffle the deck in-place.
        """
        shuffle(self.deck)

    def deal_cards(self, num_cards):
        """
                Deal a specified number of cards from the deck.

                Parameters:
                - num_cards (int): The number of cards to deal.

                Returns:
                - List[Card] or None: A list of cards dealt to the player or None if there are not enough cards.
        """
        if num_cards <= len(self.deck):
            player_hand = self.deck[:num_cards]
            self.deck = self.deck[num_cards:]
            return player_hand
        else:
            print("Not enough cards in the deck.")
            return None
