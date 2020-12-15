""" Deck module """

import random
from card import Card


class Deck:
    """ The deck class """

    def __init__(self):
        self._count = 52

        suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
        values = [str(i) for i in range(2, 11)]
        values.extend(["Jack", "King", "Queen", "Ace"])

        self._cards = []
        for suit in suits:
            for value in values:
                self._cards.append(Card(suit, value))

    @property
    def count(self):
        """ Return number of cards in deck """
        return self._count

    @property
    def cards(self):
        """ Return raw list of cards """
        return self._cards

    def shuffle(self):
        """ Shuffle the deck in place """
        random.shuffle(self._cards)

    def get_next_card(self):
        """ Get the next card off the top of the deck """

        if self._count != 0:
            self._count -= 1
            return self._cards.pop()

        raise IndexError

    def __repr__(self):
        deck_list = []
        for card in self._cards:
            deck_list.append(str(card))

        return ",".join(deck_list)
