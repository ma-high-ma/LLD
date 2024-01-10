from dao.transaction import TransactionDao


class Customer:
    def __init__(self, id, name, dob, age):
        self.id = id
        self.name = name
        self.dob = dob
        self.age = age
