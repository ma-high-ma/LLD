from constants import OrderStatus
from dao.cart_item import CartItemDao
from dao.order import OrderDao
from exceptions import OrderNotFound
from interfaces.order import OrderInterface
from services.cart import CartService
from services.product import ProductService
from services.user import UserService


class OrderService(OrderInterface):
    def create(self, id, user_id, cart_id, status, shipping_info, payment_info):
        return OrderDao().create(id, user_id, cart_id, status, shipping_info, payment_info)

    def get_order_by_id(self, id):
        try:
            return OrderDao().get_by_id(id)
        except OrderNotFound as e:
            print("Error: ", str(e))
            return None

    def get_all_orders_by_user_id(self, user_id, status=OrderStatus.COMPLETED):
        user = UserService().get_user_by_id(user_id)
        if not user:
            return
        orders = OrderDao().get_all_orders_by_user_id(user_id)
        for order in orders:
            if order.status == status:
                print(order.__dict__)
                cart_id = order.cart_id
                cart_items = CartItemDao().get_cart_items_by_cart_id(cart_id)
                CartItemDao().print(cart_items)


    def is_checkout_possible(self, user_id):
        user = UserService().get_user_by_id(user_id)
        if not user:
            print("Order cannot be placed: User not found")
            return False
        cart = CartService().get_cart_for_user(user_id=user_id)
        if not cart:
            print("Order cannot be placed: Cart not found")
            return False
        if not self.is_inventory_enough(cart):
            print("Order cannot be placed: Not enough inventory")
            return False
        return True

    def checkout(self, id, user_id, shipping_info, payment_info):
        cart = CartService().get_cart_for_user(user_id=user_id)
        order = self.create(id=id, user_id=user_id, cart_id=cart.id, status=OrderStatus.COMPLETED, payment_info=payment_info,
                    shipping_info=shipping_info)
        self.perform_post_checkout_tasks(cart_id=cart.id, user_id=user_id)
        return order


    def is_inventory_enough(self, cart):
        cart_items = CartService().get_cart_items_by_cart_id(cart.id)
        if not cart_items:
            return False
        for product_id in cart_items:
            quantity = cart_items[product_id]
            if not ProductService().is_product_available(product_id, quantity):
                return False

        return True

    def perform_post_checkout_tasks(self, cart_id, user_id):
        CartService().update_inventory_post_checkout(cart_id)
        CartService().remove_user_cart(user_id=user_id)

