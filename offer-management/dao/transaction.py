import uuid

from exceptions import TransactionNotFound
from models.transaction import Transaction


class TransactionDao:
    transaction_map = {}

    def create(self, customer_id, merchant_id, date, city, amount):
        transaction_id = uuid.uuid4()
        transaction = Transaction(id=transaction_id, customer_id=customer_id, merchant_id=merchant_id, date=date, city=city, amount=amount)
        self.transaction_map[transaction_id] = transaction
        return transaction

    def get_by_id(self, id):
        try:
            return self.transaction_map[id]
        except KeyError:
            raise TransactionNotFound(id=id)

    def get_all(self):
        transactions = []
        for id, obj in self.transaction_map.items():
            transactions.append(obj)
        return transactions

    def get_last_week_transactions(self, customer_id, start_date):
        transactions = self.get_all()
        customer_last_week_transactions = []
        amount = 0
        for transaction in transactions:
            if transaction.customer_id == customer_id and transaction.date >= start_date:
                customer_last_week_transactions.append(transaction)
                amount += transaction.amount

        return amount



