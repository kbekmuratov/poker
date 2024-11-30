from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

        for rank in Card.RANKS:
            for suit in Card.SUITS:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None
