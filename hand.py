""" This is the hand module. It holds the card class.

    Typcial usage:

    hand = Hand()
    hand.add_card(new_card)
"""


class Hand:
    """The Hand class.

    This is the class that creates a hand for a player to keep
    their collection of cards.

    Attributes:
        cards: a list of cards.
        points: the total number of points in the hand.
    """

    def __init__(self):
        self._cards = []
        self._points = 0

    def sort(self):
        """Sort the cards in a hand.

        Cards are sorted first by suit, then by value.
        """

        self._cards = sorted(self._cards, key=lambda c: (c.suit_points, c.value_points))

    @property
    def cards(self):
        """ Return raw list of cards. """
        return self._cards

    @property
    def points(self):
        """ Return list of total points. """
        return self._points

    def add_card(self, card):
        """Add a card to the player's hand .

        As a card is added, it's points are evaluated.
        """
        self._cards.append(card)
        self._points += card.suit_points * card.value_points
        self.sort()

    def __repr__(self):
        hand_list = []
        for card in self._cards:
            hand_list.append(repr(card))

        return ", ".join(hand_list)
