import uuid

from dao.transaction import TransactionDao
from exceptions import CustomerNotFound
from models.customer import Customer


class CustomerDao:
    customer_map = {}

    def create(self, name, dob, age):
        customer_id = uuid.uuid4()
        customer = Customer(id=customer_id, name=name, dob=dob, age=age)
        self.customer_map[customer_id] = customer
        return customer

    def get_by_id(self, id):
        try:
            return self.customer_map[id]
        except KeyError:
            raise CustomerNotFound(id=id)

    def spends_last_week(self, id):
        start_date = 20231216 - 7
        amount = TransactionDao().get_last_week_transactions(customer_id=id, start_date=start_date)
        return amount
