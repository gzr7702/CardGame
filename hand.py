""" The hand object """


class Hand:
    """ Hand class """

    def __init__(self):
        self._cards = []

    def sort(self, hand):
        """ Sort the cards in a hand """
        print("in sort")
        return hand

    @property
    def cards(self):
        """ Return raw list of cards """
        return self._cards

    @cards.setter
    def cards(self, card):
        """ Add a card to the player's hand """
        self._cards.append(card)
        # self.sort()

    def __repr__(self):
        hand_list = []
        for card in self._cards:
            hand_list.append(str(card))

        return ",".join(hand_list)
