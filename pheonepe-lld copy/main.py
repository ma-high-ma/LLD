from dao.product import ProductDao
from decorators.user_auth import UserAuthDecorator
from interfaces.cart import CartInterface
from interfaces.order import OrderInterface
from services.cart import CartService
from services.order import OrderService
from services.product import ProductService
from services.user import UserService

if __name__ == '__main__':
    print("Begin!")
    user0 = UserService().create(id="u0", name="Mahima", email="abc@xyz.com", password="abc")
    user1 = UserService().create(id="u1", name="Mahima", email="abc", password="abc")
    # UserService.get_user_by_id()

    print("creating products\n")
    product1 = ProductService().create(id="p0", name="Product1", price_per_unit=12.50, quantity=6)
    product2 = ProductService().create(id="p1", name="Product1", price_per_unit=12.50, quantity=2)
    ProductService().view_product(product1.id)
    # ProductService().view_product("1234")

    print()
    print("Adding to cart")
    service = UserAuthDecorator(CartService(), OrderService())
    cart = service.add_to_cart(user_id=user0.id, product_id=product1.id, quantity=3)
    print("Cart Created with id = ", cart.id)
    CartService().view_cart(user0.id)

    print()
    # cart = CartService().add_to_cart(user_id=user0.id, product_id=product1.id, quantity=3)
    cart = CartService().add_to_cart(user_id=user0.id, product_id=product1.id, quantity=1)
    CartService().view_cart(user0.id)
    print()

    invalid_cart = CartService().add_to_cart(user_id="123", product_id=product1.id, quantity=3)

    CartService().view_cart(user0.id)
    if OrderService().is_checkout_possible(user0.id):
        order = OrderService().checkout(id="o0", user_id=user0.id, shipping_info="ABC", payment_info="ABC")
        print("Order Placed with id = ", order.id)

    OrderService().get_all_orders_by_user_id(user0.id)
    OrderService().get_all_orders_by_user_id("1234")

    user1 = UserService().create(id="u1", name="Mahima", email="abc@xyz.com", password="abc")
    cart = CartService().add_to_cart(user_id=user1.id, product_id=product1.id, quantity=2)
    cart = CartService().add_to_cart(user_id=user1.id, product_id=product2.id, quantity=1)
    CartService().view_cart(user1.id)
    if OrderService().is_checkout_possible(user1.id):
        order = OrderService().checkout(id="o1", user_id=user1.id, shipping_info="ABC", payment_info="ABC")
        print("Order Placed with id = ", order.id)

    OrderService().get_all_orders_by_user_id(user1.id)



