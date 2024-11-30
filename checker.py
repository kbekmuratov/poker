class Checker:
    def check_hand(self, hand):

        ranks = [card.rank for card in hand.cards]
        suits = [card.suit for card in hand.cards]

        rank_counts = {}
        for rank in ranks:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        suit_counts = {}
        for suit in suits:
            suit_counts[suit] = suit_counts.get(suit, 0) + 1

        royal_flush_ranks = ['10', 'J', 'Q', 'K', 'A']
        if all(rank in ranks for rank in royal_flush_ranks) and len(suit_counts) == 1:
            return 'Royal Flush', 10

        sorted_ranks = sorted([self.card_to_index(rank) for rank in ranks])
        if len(set(suits)) == 1 and self.is_consecutive(sorted_ranks):
            return 'Straight Flush', 9

        if 4 in rank_counts.values():
            return 'Four of a Kind', 8

        if 3 in rank_counts.values() and 2 in rank_counts.values():
            return 'Full House', 7

        if len(suit_counts) == 1:
            return "Flush", 6

        if self.is_consecutive(sorted_ranks):
            return 'Straight', 5

        if 3 in rank_counts.values():
            return 'Three of a Kind', 4

        if list(rank_counts.values()).count(2) == 2:
            return 'Two Pairs', 3

        if 2 in rank_counts.values():
            return 'Pair', 2

        return 'High Card', 1

    def card_to_index(self, rank):
        rank_order = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        return rank_order.get(rank)

    def is_consecutive(self, ranks):
        if len(ranks) != 5:
            return False

        if ranks[4] - ranks[0] == 4:
            return True

        if ranks == [2, 3, 4, 5, 14]:
            return True

        return False
