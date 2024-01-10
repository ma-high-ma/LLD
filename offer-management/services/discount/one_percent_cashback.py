from services.discount.base import DiscountBase


class OnePercentCashback(DiscountBase):
    def compute(self):
        return 0.99 * self.amount
