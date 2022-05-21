import random

class Card():

    def suit(self):
        self.suit = ['hearts', 'diamonds', 'clubs', 'spades']
        self.value = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


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


card1 = Card()
deck_of_cards = []
for card in card1.suit:
    for i in card.value:
        card = card.suit + ' ' + card.value
        deck_of_cards.append(card)
print(deck_of_cards)


