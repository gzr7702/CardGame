""" Module that tests game play. """

import unittest
from unittest.mock import patch
from io import StringIO

from card import Card
from deck import Deck
from hand import Hand
from player import Player
import game


class TestGameObjects(unittest.TestCase):
    """ Test the game setup including the deck """

    def setUp(self):
        """ Create a card deck and two players """

        self.sample_card = Card("Clubs", "3")
        self.sample_face_card = Card("Diamonds", "King")
        self.deck = Deck()
        self.hand = Hand()

        cards = [
            ("Spades", "2"),
            ("Diamonds", "5"),
            ("Spades", "King"),
            ("Hearts", "3"),
            ("Clubs", "Ace"),
        ]

        self.unsorted_cards = ", ".join([x[1] + ":" + x[0] for x in cards])

        for card in cards:
            self.hand.add_card(Card(card[0], card[1]))

    def test_card_created_with_properties(self):
        """ Test card is created properly """

        self.assertTrue(
            (self.sample_card.suit == "Clubs") and (self.sample_card.value == "3")
        )

    def test_card_has_proper_suit_points(self):
        """ Test that a number card has proper suit points. """
        self.assertTrue(self.sample_card.suit_points, 4)

    def test_card_has_proper_value_points(self):
        """ Test that a number card has proper value points. """
        self.assertTrue(self.sample_card.value_points, 3)

    def test_face_card_has_proper_suit_points(self):
        """ Test that a face card has proper suit points. """
        self.assertTrue(self.sample_face_card.suit_points, 2)

    def test_face_card_has_proper_value_points(self):
        """ Test that a face card has proper value points. """
        self.assertTrue(self.sample_face_card.value_points, 14)

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
        player = Player("Ezra")
        self.assertEqual("Ezra", player.name)

    def test_get_next_card(self):
        """ Test that we can pull a card from the top of the deck. """

        card = self.deck.get_next_card()
        card_count = self.deck.count
        self.assertIsInstance(card, Card)
        self.assertTrue(card_count, 51)

    def test_empty_deck_returns_nothing(self):
        """ Create an empty deck to test that pulling a card will throw exception """

        deck = Deck()
        for i in range(52):
            deck.get_next_card()
        print(deck.count)

        self.assertRaises(IndexError, deck.get_next_card)

    def test_add_card_to_hand(self):
        """ Test that we can add a card to a player's hand. """

        hand = Hand()
        hand.add_card(self.sample_card)
        self.assertEqual(repr(hand), repr(self.sample_card))

    def test_cards_added_to_hand_are_sorted(self):
        """Test that cards were added to hand in order. """

        self.assertNotEqual(str(self.hand), self.unsorted_cards)

    def test_that_hand_has_correct_points(self):
        """Test that the hand object calculated the correct amount of points
        when it added new cards to the hand.
        """

        self.assertEqual(self.hand.points, 37)


class TestGame(unittest.TestCase):
    """Test the aspects of the game """

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

    @patch("builtins.input", return_value="q")
    def test_player_input(self, input):
        """ Test that the player input works. """
        command = game.get_command()
        self.assertEqual(command, "q")

    def test_game(self):
        with patch('builtins.input', return_value="p"):
            assert yes_or_no() == "score"
    '''

if __name__ == "__main__":
    unittest.main()
