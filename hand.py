""" The hand object """


class Hand:
    """ Hand class """

    def __init__(self):
        self._cards = []
        self._points = 0

    def sort(self):
        """Sort the cards in a hand.
        Cards are sorted first by suit, then by value."""

        self._cards = sorted(self._cards, key=lambda c: (c.suit_points, c.value_points))

    @property
    def cards(self):
        """ Return raw list of cards """
        return self._cards

    @property
    def points(self):
        """ Return list of total points. """
        return self._points

    def add_card(self, card):
        """ Add a card to the player's hand """
        self._cards.append(card)
        self._points += card.suit_points * card.value_points
        self.sort()

    def __repr__(self):
        hand_list = []
        for card in self._cards:
            hand_list.append(repr(card))

        return ", ".join(hand_list)
