from dao.product import ProductDao
from exceptions import ProductNotFound


class ProductService:
    def create(self, id, name, price_per_unit, quantity=1):
        return ProductDao().create(id, name, price_per_unit, quantity)

    def view_product(self, product_id):
        product = self.get_product_by_id(product_id)
        if not product:
            return
        print("Name: ", product.name, " Price Per Unit: ", product.price_per_unit)

    def get_product_by_id(self, id):
        try:
            return ProductDao().get_by_id(id)
        except ProductNotFound as e:
            print(str(e))
            return None

    def is_product_available(self, product_id, quantity=1):
        return ProductDao().is_product_available(product_id, quantity)

    def update_inventory(self, product_id, quantity, activity):
        return ProductDao().update_inventory(product_id, quantity, activity)
