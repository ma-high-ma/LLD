class CustomerNotFound(BaseException):
    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        message = f"{self.id} -> customer not found"
        return message


class TransactionNotFound(BaseException):
    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        message = f"{self.id} -> transaction not found"
        return message
