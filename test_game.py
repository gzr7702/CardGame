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

    def test_card_created_with_properties(self):
        ''' Test card is created properly '''
        self.assertTrue(self.sample_card.suit == 'clubs')
        self.assertTrue(self.sample_card.value == '3')

class TestGame(unittest.TestCase):
    ''' Test that the game can be played properly '''

if __name__ == "__main__":
    unittest.main()
