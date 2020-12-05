'''
    Tests for card game. One integrated test for the game setup, and one for the game play.
'''

import unittest

from card import Card

class TestGameSetup(unittest.TestCase):
    ''' Test the game setup including the deck '''
    def setUp(self):
        ''' Create a card deck and two players '''
        self.sample_card = Card('clubs', '3')
<<<<<<< HEAD
        self.deck = Deck()

    def test_card_created_with_properties(self):
        ''' Test card is created properly '''
        self.assertTrue((self.sample_card.suit == 'clubs') and (self.sample_card.value == '3'))

    def test_deck_is_proper_length(self):
        ''' Test deck length '''
        self.assertTrue(len(self.deck) == 52)
=======

    def test_card_created_with_properties(self):
        ''' Test card is created properly '''
        self.assertTrue(self.sample_card.suit == 'clubs')
        self.assertTrue(self.sample_card.value == '3')
>>>>>>> card_setup

class TestGame(unittest.TestCase):
    ''' Test that the game can be played properly '''

if __name__ == "__main__":
    unittest.main()
