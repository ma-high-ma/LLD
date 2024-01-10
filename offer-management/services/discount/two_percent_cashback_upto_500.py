from services.discount.base import DiscountBase


class TwoPercentUpto500Cashback(DiscountBase):
    def compute(self):
        discount = 0.02 * self.amount
        discount = min(discount, 500)
        return self.amount - discount
