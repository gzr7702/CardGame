import unittest

class TestGameSetup(unittest.TestCase):
    def setUp(self):
        ''' Create a card deck and two players '''
        self.deck = []

    def test_deck_proper_length(self):
        self.assertTrue(len(self.deck) == 52)

class TestGame(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()