""" Deck module """

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
