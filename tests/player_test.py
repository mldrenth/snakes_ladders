import unittest
from src.player import Player
from src.dice import Dice

class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player("Bob", "Yellow", 1)
        
    
    def test_position_starts_at_0(self):
        actual = self.player.position
        self.assertEqual(0, actual)
    
    def test_player_rolls_to_get_number_in_range_1_to_6(self):
        dice = Dice(6)
        numbers = range(1, 7)
        random_number = self.player.roll_dice(dice)
        self.assertIn(random_number, numbers)