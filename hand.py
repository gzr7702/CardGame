""" The hand object """


class Hand:
    """ Hand class """

    def __init__(self):
        self._cards = []

    def sort(self):
        """ Sort the cards in a hand """
        face_points =  {'Ace': 1, 'Jack': 11, 'King': 12, 'Queen': 13}

        card_dict = {'Spades': [], 'Diamonds': [], 'Hearts': [], 'Clubs': []}
        for card in self._cards:
            card_dict[card.suit].append(card.value)
        print(card_dict)

    @property
    def cards(self):
        """ Return raw list of cards """
        return self._cards

    def add_card(self, card):
        """ Add a card to the player's hand """
        self._cards.append(card)
        self.sort()

    def __repr__(self):
        hand_list = []
        for card in self._cards:
            hand_list.append(repr(card))

        return ", ".join(hand_list)
