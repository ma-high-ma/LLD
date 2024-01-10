import random


class Dice:
    def __init__(self, id, total_number):
        self.id = id
        self.total_number = total_number

    def roll(self):
        start, end = 1, 6 * self.total_number
        return random.randint(start, end)
