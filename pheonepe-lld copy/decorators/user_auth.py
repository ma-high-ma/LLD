from services.user import UserService


class UserAuthDecorator:
    def __init__(self, cart_service, order_service):
        self.cart_service = cart_service
        self.order_service = order_service

    def is_valid_user(self, user_id):
        user = UserService().get_user_by_id(user_id)
        return user

    def add_to_cart(self, user_id, product_id, quantity):
        if self.is_valid_user(user_id):
            return self.cart_service.add_to_cart(user_id, product_id, quantity)
        else:
            return None
