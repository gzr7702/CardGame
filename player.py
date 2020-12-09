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
        """ Return the player's name """
        return self._name

    def sort(self):
        pass

    @property
    def hand(self):
        """ Return the player's hand """
        return self._hand

    @hand.setter
    def hand(self, card):
        """ Add a card to the player's hand """
        self._hand.append(card)
