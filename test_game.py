""" These are the tests for card game. One integrated test for the game
    setup, and one for the game play.
"""

import unittest
from unittest.mock import patch
from io import StringIO

from card import Card
from deck import Deck
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
        p = Player()
        self.assertIsNotNone(p.name)


class TestGame(unittest.TestCase):
    """Test the aspects of the game """

    def setUp(self):
        """ Create a card deck. """

        self.deck = Deck()

    @patch("sys.stdout", new_callable=StringIO)
    def test_game_text(self, mock_stdout):
        """ Test that the game text is correct. """
        intro = (
            "Welecome! Hit any key for the next "
            + "player to take a turn, 'q' to quit.\n"
        )
        instructions = 6 * "Hit any key to continue\n"
        text = intro + instructions
        # TODO: figure out all inputs
        game.main()
        self.assertEqual(mock_stdout.getvalue(), text)

    @patch("builtins.input", return_value="q")
    def test_player_input(self, input):
        """ Test that the player input works. """
        command = game.get_command()
        self.assertEqual(command, "q")

    def test_get_next_card(self):
        """ Test that we can pull the next card on the deck. """

        card = self.deck.get_next_card()
        card_count = self.deck.count
        self.assertIsInstance(card, Card)
        self.assertTrue(card_count, 51)


if __name__ == "__main__":
    unittest.main()
