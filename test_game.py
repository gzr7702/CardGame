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

    def setUp(self):
        """ Set up mock players for game. """
        self.player1 = Player("Ezra")
        self.player2 = Player("Taylor")

        cards = [
            Card("Hearts", "3"),
            Card("Diamonds", "5"),
            Card("Hearts", "10"),
            Card("Spades", "Ace"),
            Card("Diamonds", "Jack"),
            Card("Clubs", "Queen"),
        ]

        for card1 in cards[:3]:
            self.player1.hand.add_card(card1)

        for card2 in cards[3:]:
            self.player2.hand.add_card(card2)

    @patch("builtins.input", side_effect=["Brooklyn", "Chris"])
    def test_game_setup_creates_users(self, input):
        """ Test that the setup function can create a users. """

        (player1, player2) = game.set_up()
        self.assertIsInstance(player1, Player)
        self.assertIsInstance(player2, Player)

    @patch("sys.stdout", new_callable=StringIO)
    def test_current_score_function(self, mock_stdout):
        """ Test the output of the current score function. """

        score_message = (
            "\tCurrent score for each player is:\n\t"
            + self.player1.name
            + ":"
            + str(self.player1.hand.points)
            + "\n\t"
            + self.player2.name
            + ":"
            + str(self.player2.hand.points)
            + "\n\n"
        )

        game.print_current_score(self.player1, self.player2)
        self.assertEqual(mock_stdout.getvalue(), score_message)

    @patch("sys.stdout", new_callable=StringIO)
    def test_player_turn_function(self, mock_stdout):
        """ Test that player gets a new card. """

        deck = Deck()
        player = Player("NextCardPlayer")
        next_card = deck.cards[-1]
        game.player_takes_turn(player, deck)

        self.assertEqual(repr(next_card), repr(player.hand))

    # TODO: test game_score()

    @patch("sys.stdout", new_callable=StringIO)
    def test_end_game_function(self, mock_stdout):
        """ Test that the end of game function displays the proper text. """

        game.end_game(self.player1, self.player2)

        function_text = (
            "\tThe final score is:\n\t"
            + self.player1.name
            + ":"
            + str(self.player1.hand.points)
            + "\n\t"
            + self.player2.name
            + ":"
            + str(self.player2.hand.points)
            + "\n\n"
            + "The winner is "
            + self.player2.name
            + " With "
            + str(self.player2.hand.points)
            + " points!\n\n"
        )

        self.assertEqual(mock_stdout.getvalue(), function_text)

    @patch("builtins.input", side_effect=["Test_name1", "Test_name2", "q"])
    def test_player_can_quit(self, input):
        """ Test that the player can quit and the app exits gracefully. """
        with self.assertRaises(SystemExit) as system_exit:
            game.main()
        self.assertEqual(system_exit.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
