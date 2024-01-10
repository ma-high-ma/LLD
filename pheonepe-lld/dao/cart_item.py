from exceptions import CartNotFound


class CartItemDao:
    CartIdToItemMap = {}
    """
    {
        "cart_id": {
            "product1": 1,
            "product2": 3
        }
    }
    """

    def create_or_update(self, cart_id, product_id, quantity):
        if not self.CartIdToItemMap.get(cart_id):
            self.CartIdToItemMap[cart_id] = {}

        if not self.CartIdToItemMap[cart_id].get(product_id):
            self.CartIdToItemMap[cart_id][product_id] = 0
        self.CartIdToItemMap[cart_id][product_id] += quantity

    def get_cart_items_by_cart_id(self, cart_id):
        try:
            return self.CartIdToItemMap[cart_id]
        except KeyError:
            raise CartNotFound(cart_id)
