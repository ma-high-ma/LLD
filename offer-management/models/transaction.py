class Transaction:
    def __init__(self, id, customer_id, merchant_id, date, city, amount):
        self.id = id
        self.customer_id = customer_id
        self.merchant_id = merchant_id
        self.date = date
        self.city = city
        self.amount = amount
