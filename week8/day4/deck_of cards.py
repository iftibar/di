import random


class Card():
    def __init__(self, val, suit):
        self.suit = suit
        self.val = val


class Deck():
    def __init__(self, deck):
        self.deck = deck

    def shuffle(self):
        if len(self.deck) == 52:
            random.shuffle(self.deck)

    def deal(self):
        card_to_deal = random.choice(self.deck)
        self.deck.remove(card_to_deal)
        return card_to_deal


suit = ['hearts', 'diamonds', 'clubs', 'spades']
val = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

deck_of_cards = [Card(val, s) for val in range(1, 14) for s in suit]
print(Card(11, 'spades'))
