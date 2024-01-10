from services.discount.base import DiscountBase


class Flat500Cashback(DiscountBase):
    def compute(self):
        discount = 500
        return self.amount - discount
