from constants import EligibilityEntity, EligibilityCondition
from dao.customer import CustomerDao
from dao.eligibility_criteria import EligibilityCriteriaDao
from dao.offer import OfferDao
from resolvers.discount import DiscountByTypeResolver
from services.customer import CustomerService
from services.transaction import TransactionService


class OfferManagementService:
    def create_offer(self, name, eligibility_criteria_list, discount):
        return OfferDao().create(name, eligibility_criteria_list, discount)

    def create_eligibility_criteria(self, entity, key, value, condition):
        return EligibilityCriteriaDao().create(entity, key, value, condition)

    def __check_customer_eligibility(self, customer, eligibility_criteria):
        if eligibility_criteria.key == "spends_last_week":
            customer_attr = CustomerDao().spends_last_week(customer.id)
        else:
            customer_attr = getattr(customer, eligibility_criteria.key)
        if eligibility_criteria.condition == EligibilityCondition.GREATER_THAN:
            return customer_attr > eligibility_criteria.value
        elif eligibility_criteria.condition == EligibilityCondition.LESSER_THAN:
            return customer_attr < eligibility_criteria.value
        elif eligibility_criteria.condition == EligibilityCondition.EQUAL_TO:
            return customer_attr == eligibility_criteria.value

    def __check_transaction_eligibility(self, transaction, eligibility_criteria):
        transaction_attr = getattr(transaction, eligibility_criteria.key)
        if eligibility_criteria.condition == EligibilityCondition.GREATER_THAN:
            return transaction_attr > eligibility_criteria.value
        elif eligibility_criteria.condition == EligibilityCondition.LESSER_THAN:
            return transaction_attr < eligibility_criteria.value
        elif eligibility_criteria.condition == EligibilityCondition.EQUAL_TO:
            return transaction_attr == eligibility_criteria.value

    def is_eligibility_satisfied(self, eligibility_criteria, customer=None, transaction=None):
        if eligibility_criteria.key == "all":
            return True
        if eligibility_criteria.entity == EligibilityEntity.CUSTOMER:
            return self.__check_customer_eligibility(customer, eligibility_criteria)
        elif eligibility_criteria.entity == EligibilityEntity.TRANSACTION:
            return self.__check_transaction_eligibility(transaction, eligibility_criteria)

    def get_eligible_offers(self, transaction_id):
        transaction = TransactionService().get_by_id(transaction_id)
        customer = CustomerService().get_by_id(transaction.customer_id)
        if not transaction or not customer:
            return
        all_offers = OfferDao().get_all()
        eligible_offers = []
        for offer in all_offers:
            eligible = True
            for eligibility_criteria in offer.eligibility_criteria_list:
                if not self.is_eligibility_satisfied(eligibility_criteria, customer, transaction):
                    eligible = False
                    break
            if not eligible:
                continue
            else:
                eligible_offers.append(offer)

        if not eligible_offers:
            print("No Offer found")
        else:
            for offer in eligible_offers:
                self.print_offers(transaction.id, offer, transaction.amount)
        print("---")

    def compute_resulting_amount(self, offer, amount):
        discount_class = DiscountByTypeResolver.get_obj(discount_type=offer.discount)
        return discount_class(amount).compute()

    def print_offers(self, transaction_id, offer, amount):
        print("eligible offer found for transaction ID ", transaction_id)
        print(offer.name)
        print("amount = ", amount)
        print("discounted_amount = ", self.compute_resulting_amount(offer, amount))
        print()
