from constants import InventoryActivity
from exceptions import UserNotFound, ProductNotFound
from models.product import Product


class ProductDao:
    ProductMap = {}
    ProductInventory = {}

    def get_by_id(self, id):
        try:
            return self.ProductMap[id]
        except KeyError:
            raise ProductNotFound(id=id)

    def create(self, id, name, price_per_unit, quantity):
        product = Product(id, name, price_per_unit)
        self.ProductMap[product.id] = product
        self.update_inventory(product_id=product.id, quantity=quantity, activity=InventoryActivity.ADD)
        return product

    def update_inventory(self, product_id, quantity, activity):
        if activity == InventoryActivity.ADD:
            if not self.ProductInventory.get(product_id):
                self.ProductInventory[product_id] = 0
            self.ProductInventory[product_id] += quantity
        elif activity == InventoryActivity.REMOVE:
            self.ProductInventory[product_id] -= quantity
        return

    def is_product_available(self, product_id, quantity):
        return self.ProductInventory[product_id] >= quantity
