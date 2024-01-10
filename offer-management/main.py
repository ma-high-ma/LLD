from constants import EligibilityEntity, EligibilityCondition, DiscountTypes
from services.bank_management import BankManagementService
from services.offer_management import OfferManagementService

if __name__ == '__main__':
    # Create customer
    customer = BankManagementService().create_customer(name="cust1", dob=20011201, age=24)

    # Create eligibility criteria
    customer_age_ec = OfferManagementService().create_eligibility_criteria(entity=EligibilityEntity.CUSTOMER, key="age",
                                                                           value=15,
                                                                           condition=EligibilityCondition.GREATER_THAN)
    transaction_amount_ec = OfferManagementService().create_eligibility_criteria(entity=EligibilityEntity.TRANSACTION,
                                                                                 key="amount", value=1000,
                                                                                 condition=EligibilityCondition.GREATER_THAN)
    transaction_city_ec = OfferManagementService().create_eligibility_criteria(entity=EligibilityEntity.TRANSACTION,
                                                                               key="city", value="BLR",
                                                                               condition=EligibilityCondition.EQUAL_TO)
    all_transactions_ec = OfferManagementService().create_eligibility_criteria(entity=EligibilityEntity.TRANSACTION,
                                                                               key="all", value="all",
                                                                               condition=EligibilityCondition.EQUAL_TO)
    customer_last_week_spends_ec = OfferManagementService().create_eligibility_criteria(entity=EligibilityEntity.CUSTOMER, key="spends_last_week", value=1000, condition=EligibilityCondition.GREATER_THAN)

    # Create offers
    offer1_name = "2% cashback up to 500 on transaction > 1000 made in BLR"
    offer2_name = "1% cashback for customers with age > 15"
    offer3_name = "1% cashback for all transactions"
    offer4_name = "spend 1000 in a week and get 500 cashback"
    offer1 = OfferManagementService().create_offer(name=offer1_name, eligibility_criteria_list=[transaction_amount_ec,
                                                                                                transaction_city_ec],
                                                   discount=DiscountTypes.TWO_PERCENT_UPTO_500)
    offer2 = OfferManagementService().create_offer(name=offer2_name, eligibility_criteria_list=[customer_age_ec],
                                                   discount=DiscountTypes.ONE_PERCENT)
    offer3 = OfferManagementService().create_offer(name=offer3_name, eligibility_criteria_list=[all_transactions_ec],
                                                   discount=DiscountTypes.ONE_PERCENT)
    offer4 = OfferManagementService().create_offer(name=offer4_name, eligibility_criteria_list=[customer_last_week_spends_ec],
                                                   discount=DiscountTypes.FLAT_500)

    # Create Transactions
    BankManagementService().show_all_transactions()
    transaction1 = BankManagementService().create_transaction(customer.id, 123, 20231216, "BLR", 500)

    BankManagementService().show_all_transactions()
    transaction2 = BankManagementService().create_transaction(customer.id, 123, 20231216, "BLR", 1500)

    # Get offers
    OfferManagementService().get_eligible_offers(transaction1.id)
    OfferManagementService().get_eligible_offers(transaction2.id)
