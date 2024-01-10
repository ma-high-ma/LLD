class OfferStatus:
    ACTIVE = "active"


class EligibilityEntity:
    CUSTOMER = "customer"
    TRANSACTION = "transaction"


class EligibilityCondition:
    GREATER_THAN = "greater_than"
    EQUAL_TO = "equal_to"
    LESSER_THAN = "lesser_than"


class DiscountTypes:
    ONE_PERCENT = "one_percent"
    TWO_PERCENT_UPTO_500 = "two_percent_upto_500"
    FLAT_500 = "flat_500"
