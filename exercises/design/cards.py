# -*- coding: utf-8 -*-

import random


class Card(object):

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank], 
                                 Card.suit_names[self.suit])

    def __cmp__(self, other):
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return cmp(t1, t2)


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in xrange(4):
            for rank in xrange(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def pop_card(self, ind=-1):
        return self.cards.pop(ind)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in xrange(num):
            hand.add_card(self.pop_card())


class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.label = label


class PokerHand(Hand):

    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def compute_frequencies(self):
        self.suits = Frequence()
        self.ranks = Frequence()

        for card in self.cards:
            self.suits.count(card.suit)
            self.ranks.count(card.rank)

        self.rank_freq = self.ranks.values()
        self.rank_freq.sort(reverse=True)

    def check_freq(self, *requirement):
        for need, have in zip(requirement, self.rank_freq):
            if need > have:
                return False
        return True

    def has_highcard(self):
        return len(self.cards)

    def has_pair(self):
        """Checks whether this hand has a pair."""
        return self.check_freq(2)

    def has_twopair(self):
        """Checks whether this hand has two pair."""
        return self.check_freq(2, 2)

    def has_threekind(self):
        """Checks whether this hand has three of a kind."""
        return self.check_freq(3)

    def has_fourkind(self):
        """Checks whether this hand has four of a kind."""
        return self.check_freq(4)

    def has_fullhouse(self):
        """Checks whether this hand has a full house."""
        return self.check_freq(3, 2)

    def has_flush(self):
        """Checks whether this hand has a flush."""
        for val in self.suits.values():
            if val > 5:
                return True
        return False

    def has_straight(self):
        """Checks whether this hand has a straight."""
        ranks = self.ranks.copy()
        # Ace can follow king to form a straight.
        ranks[14] = ranks.get(1, 0)

        return self._check_in_a_row(ranks, 5)

    def _check_in_a_row(self, ranks, num):
        """Checks whether the hand has num ranks in a row."""
        count = 0
        for i in xrange(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == num:
                    return True
            else:
                count = 0
        return False

    def has_straightflush(self):
        """Checks whether this hand has a straight flush."""
        # Partition the hand by suit and check each
        # sub-hand for a straight.
        partition = {}
        for card in self.cards:
            partition.setdefault(card.suit, PokerHand()).add_card(card)

        for hand in partition.values():
            if len(hand.cards) < 5:
                continue
            hand.compute_frequencies()
            if hand.has_straight():
                return True
        return False

    def classify(self):
        self.compute_frequencies()

        self.labels = []
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.labels.append(label)


class Frequence(dict):
    """A map from each item (x) to its frequency."""

    def __init__(self, seq=[]):
        for x in seq:
            self.count(x)

    def count(self, x, freq=1):
        self[x] = self.get(x, 0) + freq
        if self[x] == 0:
            del self[x]



if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = PokerHand()

    deck.move_cards(hand, 5)
    hand.sort()
    print hand
    hand.classify()
    print hand.labels

