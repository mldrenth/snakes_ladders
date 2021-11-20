import unittest
from src.board import Board

class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board(100)
    
    def test_board_has_squares(self):
        actual = self.board.number_of_squares
        expected = 100
        self.assertEqual(expected, actual)
    
    def test_board_can_access_modifiers(self):
        actual = self.board.get_modifier(60)
        expected = -30
        self.assertEqual(expected,actual)