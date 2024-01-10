from services.customer import CustomerService
from services.transaction import TransactionService


class BankManagementService:
    def create_customer(self, name, dob, age):
        return CustomerService().create_customer(name, dob, age)

    def create_transaction(self, customer_id, merchant_id, date, city, amount):
        return TransactionService().create_transaction(customer_id, merchant_id, date, city, amount)

    def show_all_transactions(self):
        print("ALL Transactions")
        TransactionService().print_all()
        print("---")


