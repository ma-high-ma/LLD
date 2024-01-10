from exceptions import DiceNotFoundException
from models.dice import Dice


class DiceDao:
    DiceMap = {}

    def get_by_id(self, id):
        try:
            return self.DiceMap[id]
        except KeyError:
            raise DiceNotFoundException

    def create(self, id, total_number):
        dice = Dice(id, total_number)
        self.DiceMap[dice.id] = dice
        return dice
