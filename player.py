""" The module that holds the player object """

import random

from hand import Hand

names = ["Millicent", "Ciot", "Bilbo", "Lana", "Lonnie", "Bennie", "Ezekial"]


class Player:
    """ Player object """

    def __init__(self):
        self._name = random.choice(names)
        self._hand = Hand()

    @property
    def name(self):
        """ Return the player's name """
        return self._name

    @property
    def hand(self):
        """ Return the player's hand """
        return self._hand
