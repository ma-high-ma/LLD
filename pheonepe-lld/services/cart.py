from constants import InventoryActivity
from dao.cart import CartDao
from dao.cart_item import CartItemDao
from exceptions import CartNotFound
from services.product import ProductService
from services.user import UserService


class CartService:

    def create(self, id, user_id):
        return CartDao().create(id=id, user_id=user_id)

    def get_cart_for_user(self, user_id):
        try:
            return CartDao().get_by_user_id(user_id)
        except CartNotFound as e:
            print("Error: ", str(e))
            return None

    def create_cart_item(self, cart_id, product_id, quantity):
        cart_item = CartItemDao().create_or_update(cart_id=cart_id, product_id=product_id, quantity=quantity)
        return cart_item

    def can_add_to_cart(self, user_id):
        user = UserService().get_user_by_id(user_id)
        if not user:
            return False
        return True

    def add_to_cart(self, user_id, product_id, quantity):
        if not self.can_add_to_cart(user_id):
            return
        cart = self.get_cart_for_user(user_id)
        if not cart:
            id = f"cart-{user_id}"

            cart = self.create(id=id, user_id=user_id)

        cart_item = self.create_cart_item(cart_id=cart.id, product_id=product_id, quantity=quantity)
        return cart

    def get_cart_items_by_cart_id(self, cart_id):
        try:
            return CartItemDao().get_cart_items_by_cart_id(cart_id)
        except CartNotFound as e:
            print("Error: ", str(e))
            return None

    def view_cart(self, user_id):
        cart = self.get_cart_for_user(user_id)
        if not cart:
            return
        cart_items = self.get_cart_items_by_cart_id(cart_id=cart.id)
        if not cart_items:
            return
        for product_id in cart_items:
            product = ProductService().get_product_by_id(product_id)
            message = f"Product Name: {product.name} Quantity: {cart_items[product_id]}"
            print(message)

    def update_inventory_post_checkout(self, cart_id):
        cart_items = CartItemDao().get_cart_items_by_cart_id(cart_id)
        for product_id in cart_items:
            quantity = cart_items[product_id]
            ProductService().update_inventory(product_id=product_id, quantity=quantity,
                                              activity=InventoryActivity.REMOVE)

    def remove_user_cart(self, user_id):
        return CartDao().remove_from_user_cart_mapping(user_id)
