from constants import DiscountTypes
from services.discount.flat_500 import Flat500Cashback
from services.discount.one_percent_cashback import OnePercentCashback
from services.discount.two_percent_cashback_upto_500 import TwoPercentUpto500Cashback


class DiscountByTypeResolver:
    discount_service_by_type = {
        DiscountTypes.ONE_PERCENT: OnePercentCashback,
        DiscountTypes.TWO_PERCENT_UPTO_500: TwoPercentUpto500Cashback,
        DiscountTypes.FLAT_500: Flat500Cashback
    }

    @classmethod
    def get_obj(cls, discount_type):
        try:
            discount_type_class = cls.discount_service_by_type[discount_type]
            return discount_type_class
        except KeyError:
            raise KeyError
