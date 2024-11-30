class Hand:
    def __init__(self):
        self.cards = []

    def add_cards(self, card):
        self.cards.append(card)

    def replace_card(self, index, card):
        if 0 <= index < len(self.cards):
            self.cards[index] = card

    def show_hand(self):
        print('|', end=' ')
        for i in range(len(self.cards)):
            print(str(i+1).ljust(5), end='| ')
        print()

        print('|', end=' ')
        for card in self.cards:
            print(str(card).ljust(5), end='| ')
        print('')
