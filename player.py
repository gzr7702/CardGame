""" The module that holds the player object """

import random

from hand import Hand

class Player:
    """ Player object """

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
