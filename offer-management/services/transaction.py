from dao.transaction import TransactionDao
from exceptions import TransactionNotFound


class TransactionService:
    def create_transaction(self, customer_id, merchant_id, date, city, amount):
        return TransactionDao().create(customer_id, merchant_id, date, city, amount)

    def get_by_id(self, id):
        try:
            return TransactionDao().get_by_id(id)
        except TransactionNotFound as e:
            print("Error: ", str(e))
            return None

    def print_all(self):
        transactions = TransactionDao().get_all()
        for transaction in transactions:
            print(transaction.__dict__)



