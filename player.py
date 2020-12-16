""" This module holds the player object.

    Typical usage:

    player = player
"""

from hand import Hand


class Player:
    """Player object.

    This clases holds the player object. The name is passed in as a parameter.

    Attributes:
        name: The name of the player.
        hand: The hand that belongs to the player.
    """

    def __init__(self, name):
        self._name = name
        self._hand = Hand()

    @property
    def name(self):
        """ Return the player's name """
        return self._name

    @property
    def hand(self):
        """ Return the player's hand """
        return self._hand
