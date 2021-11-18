import unittest
from src.dice import Dice

class DiceTest(unittest.TestCase):

    def setUp(self):
        self.dice = Dice(6)
    
    def test_dice_has_num_of_sides(self):
        result = 6
        actual = self.dice.num_of_sides
        self.assertEqual(result, actual)

    def test_get_number__between_1_and_6(self):
        numbers = range(1, 7)
        random_number = self.dice.generate_number()
        self.assertIn(random_number, numbers)

    