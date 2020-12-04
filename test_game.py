'''
    Tests for card game. One integrated test for the game setup, and one for the game play.
'''

import unittest

class TestGameSetup(unittest.TestCase):
    ''' Test the game setup including the deck '''
    def setUp(self):
        ''' Create a card deck and two players '''
        self.deck = []

    def test_deck_proper_length(self):
        ''' Is the deck the proper length? '''
        self.assertTrue(len(self.deck) == 52)

class TestGame(unittest.TestCase):
    ''' Test that the game can be played properly '''

if __name__ == "__main__":
    unittest.main()
