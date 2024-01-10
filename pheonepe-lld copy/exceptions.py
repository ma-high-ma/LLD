class UserNotFound(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"{self.id} -> User Not Found"


class OrderNotFound(Exception):
    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        return f"{self.id} -> Order Not Found"


class CartNotFound(Exception):
    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        return f"{self.id} -> Cart Not Found"


class ProductNotFound(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"{self.id} -> Product Not Found"
