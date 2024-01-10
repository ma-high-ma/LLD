from constants import CartStatus
from exceptions import UserNotFound, CartNotFound
from models.cart import Cart


class CartDao:
    CartMap = {}
    UserCartMap = {}

    def get_by_id(self, id):
        try:
            return self.CartMap[id]
        except KeyError:
            raise CartNotFound(id=id)

    def get_by_user_id(self, user_id):
        try:
            return self.UserCartMap[user_id]
        except KeyError:
            raise CartNotFound

    def create(self, user_id, id):
        cart = Cart(id=id, status=CartStatus.ACTIVE)
        self.CartMap[cart.id] = cart
        self.add_to_user_cart_map(user_id, cart)
        return cart

    def add_to_user_cart_map(self, user_id, cart_id):

        self.UserCartMap[user_id] = cart_id
        return

    def remove_from_user_cart_mapping(self, user_id):
        return self.UserCartMap.pop(user_id, None)


