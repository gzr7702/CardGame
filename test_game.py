""" Module that tests game play. """

import unittest
from unittest.mock import patch

from card import Card
from deck import Deck
from hand import Hand
from player import Player
import game


class TestGame(unittest.TestCase):
    """Test the aspects of the game """

    def setUp(self):
        """ Create a card deck. """

        self.sample_card = Card("Hearts", "7")
        self.deck = Deck()
        self.player = Player()
        self.hand = Hand()

    '''
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
    '''

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

    def test_player_sort_method(self):

        unsorted_cards = [
            Card("Spades", "2"),
            Card("Diamonds", "5"),
            Card("Spades", "King"),
            Card("Hearts", "3"),
            Card("Clubs", "Ace"),
        ]

        sorted_cards = self.hand.sort(unsorted_cards)
        import pdb; pdb.set_trace()
        self.assertNotEqual(unsorted_cards, sorted_cards)

    '''
    def test_add_card_to_hand(self):
        """ Test that we can add a card to a player's hand. """

        self.hand.cards.append(self.sample_card)
        self.assertEqual(self.hand, [self.sample_card])
    '''

if __name__ == "__main__":
    unittest.main()
