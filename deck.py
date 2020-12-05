""" Deck module """

from card import Card

suits = ["clubs", "hearts", "diamonds", "spades"]
values = [str(i) for i in range(1, 11)]
values.extend(["Jack", "King", "Queen", "Ace"])


class Deck:
    """ The deck class """

    def __init__(self):
        self._count = 52

        card = Card("spades", "ace")
        self._cards = [card] * self._count

    @property
    def count(self):
        """ Return number of cards in deck """
        return self._count

    @property
    def cards(self):
        """ Return list of cards """
        return self._cards
