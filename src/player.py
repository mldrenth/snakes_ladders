class Player:
    def __init__(self, name, counter_colour, turn):
        self.name = name
        self.counter_colour = counter_colour
        self.turn = turn
        self.position = 0
    
    def roll_dice(self,dice):
        return dice.generate_number()