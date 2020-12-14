""" This is the card module.

For each card, we hold the suit and value, as well as the points for each.
"""


class Card:
    """ The card class """

    def __init__(self, suit, value):
        # Maps that hold the integer values of face cards and suits
        face_points_map = {"Ace": 1, "Jack": 11, "King": 12, "Queen": 13}
        suit_points_map = {"Spades": 1, "Diamonds": 2, "Hearts": 3, "Clubs": 4}

        self._suit = suit
        self._suit_points = suit_points_map[suit]

        self._value = value

        if value in face_points_map.keys():
            self._value_points = face_points_map[value]
        else:
            self._value_points = int(value)

    @property
    def suit(self):
        """ get suit """
        return self._suit

    @property
    def suit_points(self):
        """ get suit points """
        return self._suit_points

    @property
    def value(self):
        """ get value """
        return self._value

    @property
    def value_points(self):
        """ get value points """
        return self._value_points

    def __str__(self):
        return str(self._value) + " of " + str(self._suit)

    def __repr__(self):
        return str(self._value) + ":" + str(self._suit)
