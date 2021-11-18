import random

class Dice:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
    
    def generate_number(self):
        return random.randint(1, self.num_of_sides)
