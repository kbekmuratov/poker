from deck import Deck
from hand import Hand
from checker import Checker
from stats import Stats
import sys


class Application:
    def __init__(self):
        self.deck = Deck()
        self.checker = Checker()
        self.stats = Stats()

    def run(self):
        print('='*50)
        print(''*10 + 'Welcome to a Video Poker game!')
        print('='*50)
        print('Try to get best combinations and be a champion.')
        name = str(input('Enter your name:  '))
        print(f'Good luck {name}!')
        while True:
            self.deck.shuffle()
            player_hand = Hand()
            for _ in range(5):
                player_hand.add_cards(self.deck.deal_card())

            print('\n Your cards: ')
            player_hand.show_hand()

            replace_input = input(
                f'\n>>> {name} enter the card number to replace (separated by a space) or press Enter to skip: ')
            if replace_input.strip():
                try:
                    indices = [
                        int(num) - 1 for num in replace_input.split() if 0 < int(num) <= 5]
                    for index in indices:
                        player_hand.replace_card(index, self.deck.deal_card())
                except ValueError:
                    print('Error not correct command')
                    continue

            print('\n Replaced cards:')
            player_hand.show_hand()

            result, points = self.checker.check_hand(player_hand)
            print(f'\n>>> {name} Your result is : {result} ({points} points)')

            self.stats.update_stats(result)

            while True:
                print(
                    '\n>>> stats - for see your statistics, \n>>> play - to start new game  \n>>> exit - for finish game: ')
                next_action = input().strip().lower()
                if next_action == 'stats':
                    self.stats.show_stats()
                elif next_action == 'play':
                    break
                elif next_action == 'exit':
                    print(f'Thanks for game {name}')
                    sys.exit()
                else:
                    print('Error command')


if __name__ == '__main__':
    app = Application()
    app.run()
