""" This is the card module. It holds the card class.

    Typical usage:

    card = Card()
"""


class Card:
    """The card class.

    This is the class that holds the card object.

    Attributes:
        suit: The card suit.
        value: The card value.
        suit_points: The points that the suit is worth.
        value_points: The points that the value of the card is worth.
    """

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
        """ return suit """
        return self._suit

    @property
    def suit_points(self):
        """ return suit points """
        return self._suit_points

    @property
    def value(self):
        """ return value """
        return self._value

    @property
    def value_points(self):
        """ return value points """
        return self._value_points

    def __str__(self):
        return str(self._value) + " of " + str(self._suit)

    def __repr__(self):
        return str(self._value) + ":" + str(self._suit)
