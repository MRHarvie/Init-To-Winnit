from cards_classes import DeckOfCards


def game_top():
    print("Card Dealer\n\nI have shuffled a deck of 52 cards.\n")


def cards_left(deck):
    print()
    print(f"There are {len(deck.deck)} cards left in the deck")
    print()
    print("Good luck!")


def main():
    deck = DeckOfCards()
    deck.shuffle_deck()
    game_top()
    user_choice = int(input("How many cards would you like to draw?: "))

    if deck.deck:
        drawn_cards = deck.deal_cards(user_choice)

        if drawn_cards:
            print("Here are your cards:")
            for card in drawn_cards:
                print(f"{card.rank} of {card.suit}")
            cards_left(deck)
        else:
            print("No cards left in the deck.")
    else:
        print("No cards in the deck.")


if __name__ == "__main__":
    main()
