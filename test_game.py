"""
    Tests for card game. One integrated test for the game setup, and one for the game play.
"""

import unittest

from card import Card
from deck import Deck


class TestGameSetup(unittest.TestCase):
    """ Test the game setup including the deck """

    def setUp(self):
        """ Create a card deck and two players """
        self.sample_card = Card("clubs", "3")
        self.deck = Deck()

    def test_card_created_with_properties(self):
        """ Test card is created properly """
        self.assertTrue(
            (self.sample_card.suit == "clubs") and (self.sample_card.value == "3")
        )

    def test_card_str_method(self):
        """ Test card.__str__ exists and has the proper text """
        card_str = "3 of Clubs"
        self.assertTrue(str(self.sample_card), card_str)

    def test_deck_is_proper_length(self):
        """ Test deck length """
        self.assertTrue(self.deck.count == 52)

    def test_deck_has_all_suits(self):
        """ Check deck suits """
        suit_count = {"Clubs": 0, "Hearts": 0, "Diamonds": 0, "Spades": 0}

        # count cards in all suits
        for card in self.deck.cards:
            suit_count[card.suit] += 1

        # assert that each suit has all cards
        for card_count in suit_count.values():
            self.assertEqual(card_count, 13)

    def test_deck_has_been_shuffled(self):
        """Create a list of indeces for the ordered deck, then do the
        same for the shuffled deck and assert that they are different"""

        unshuffled_deck = repr(self.deck)
        self.deck.shuffle()
        shuffled_deck = repr(self.deck)

        self.assertFalse(unshuffled_deck == shuffled_deck)


class TestGame(unittest.TestCase):
    """ Test that the game can be played properly """


if __name__ == "__main__":
    unittest.main()
