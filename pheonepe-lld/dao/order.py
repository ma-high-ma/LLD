from exceptions import OrderNotFound
from models.order import Order


class OrderDao:
    
    OrderMap = {}
    UserOrderMap = {}

    def get_by_id(self, id):
        try:
            return self.OrderMap[id]
        except KeyError:
            raise OrderNotFound(id=id)

    def create(self, id, user_id, cart_id, status, shipping_info, payment_info):
        order = Order(id, cart_id, status, shipping_info, payment_info)
        self.OrderMap[order.id] = order
        self.add_to_user_order_map(user_id, order)
        return order

    def add_to_user_order_map(self, user_id, order_id):
        if not self.UserOrderMap.get(user_id):
            self.UserOrderMap[user_id] = []
        self.UserOrderMap[user_id].append(order_id)
        return

    def get_all_orders_by_user_id(self, user_id):
        try:
            return self.UserOrderMap[user_id]
        except KeyError:
            raise OrderNotFound()