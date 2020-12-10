""" This is the card module """


class Card:
    """ The card class """

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        """ get suit """
        return self._suit

    @property
    def value(self):
        """ get value """
        return self._value

    def __str__(self):
        return str(self._value) + " of " + str(self._suit)

    def __repr__(self):
        return str(self._value) + " " + str(self._suit)
