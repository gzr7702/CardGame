""" These are the tests for card game. One integrated test for the game
    setup, and one for the game play.
"""

import unittest
from unittest.mock import patch
from io import StringIO

from card import Card
from deck import Deck
from hand import Hand
from player import Player
import game


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
        """ Check deck all suits with 13 cards each """

        suit_count = {"Clubs": 0, "Hearts": 0, "Diamonds": 0, "Spades": 0}

        # count cards in all suits
        for card in self.deck.cards:
            suit_count[card.suit] += 1

        # assert that each suit has all cards
        for card_count in suit_count.values():
            self.assertEqual(card_count, 13)

    def test_deck_has_been_shuffled(self):
        """Compare string of unshuffled and shuffled deck. We aren't
        checking if the deck is in random order. We trust that the
        the shuffle method takes care of that"""

        unshuffled_deck = repr(self.deck)
        self.deck.shuffle()
        shuffled_deck = repr(self.deck)

        self.assertFalse(unshuffled_deck == shuffled_deck)

    def test_player_has_a_name(self):
        """ Test we can create a player and he has a name. """
        player = Player()
        self.assertIsNotNone(player.name)


if __name__ == "__main__":
    unittest.main()
