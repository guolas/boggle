import unittest
from boggle import Boggle

class TestBoggle(unittest.TestCase):
    
    def setUp(self):
        self.board = Boggle('./4x4_board.txt')

    def tearDown(self):
        self.board = None

    def test_board_size(self):
        self.assertEqual(len(self.board.letters), 16)

    def test_word_in_board(self):
        self.assertTrue(self.board.find_word('alien'))
        self.assertTrue(self.board.find_word('tane'))
        self.assertTrue(self.board.find_word('genitals'))

    def test_word_not_in_board(self):
        self.assertFalse(self.board.find_word('zambapollos'))
        self.assertFalse(self.board.find_word('caradura'))
        self.assertFalse(self.board.find_word('fuoiuas'))

if __name__ == '__main__':
        unittest.main()
