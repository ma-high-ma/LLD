class Order:
    def __init__(self, id, cart_id, status, shipping_info, payment_info):
        self.id = id
        self.cart_id = cart_id
        self.status = status
        self.shipping_info = shipping_info
        self.payment_info = payment_info
