from dao.dice import DiceDao
from exceptions import DiceNotFoundException


class DiceService:
    def create(self, id, total_number):
        return DiceDao().create(id, total_number)

    def get_by_id(self, id):
        try:
            return DiceDao().get_by_id(id)
        except DiceNotFoundException as e:
            print("Error: ", str(e))
            return None
