""" The module that holds the player object """

import random

names = ["Millicent", "Ciot", "Bilbo", "Lana", "Ken", "Bennie", "Ezekial"]


class Player:
    """ Player object """

    def __init__(self):
        self._name = random.choice(names)
        self._hand = []

    @property
    def name(self):
        return self._name

    @property
    def hand(self):
        # TODO Add sort
        return self._hand
