class Board:
    def __init__(self, number_of_squares):
        self.number_of_squares = number_of_squares
        self._modifiers = {
            2: 20,
            10: 5,
            32: -7,
            45: -20,
            60: -30,
            75: 15

        }
    
    def get_modifier(self,position):
        return self._modifiers[position]
