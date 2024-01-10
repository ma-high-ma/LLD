from dao.product import ProductDao
from services.cart import CartService
from services.order import OrderService
from services.product import ProductService
from services.user import UserService

if __name__ == '__main__':
    print("Begin!")
    user0 = UserService().create(id="u0", name="Mahima", email="abc@xyz.com", password="abc")
    # UserService.get_user_by_id()

    product1 = ProductService().create(id="p0", name="Product1", price_per_unit=12.50, quantity=6)
    product2 = ProductService().create(id="p1", name="Product1", price_per_unit=12.50, quantity=2)
    ProductService().view_product(product1.id)
    # ProductService().view_product("1234")

    cart = CartService().add_to_cart(user_id=user0.id, product_id=product1.id, quantity=3)
    cart = CartService().add_to_cart(user_id=user0.id, product_id=product1.id, quantity=1)
    print("Cart Created with id = ", cart.id)
    invalid_cart = CartService().add_to_cart(user_id="123", product_id=product1.id, quantity=3)

    CartService().view_cart(user0.id)
    if OrderService().is_checkout_possible(user0.id):
        order = OrderService().checkout(id="o0", user_id=user0.id, shipping_info="ABC", payment_info="ABC")
        print("Order Placed with id = ", order.id)

    OrderService().get_all_orders_by_user_id(user0.id)
    OrderService().get_all_orders_by_user_id("1234")



