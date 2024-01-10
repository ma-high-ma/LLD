import uuid

from constants import OfferStatus
from models.offer import Offer


class OfferDao:
    offer_map = {}

    def create(self, name, eligibility_criteria_list, discount, status=OfferStatus.ACTIVE):
        offer_id = uuid.uuid4()
        offer = Offer(id=offer_id, name=name, eligibility_criteria_list=eligibility_criteria_list, discount=discount, status=status)
        self.offer_map[offer_id] = offer
        return offer

    def get_all(self):
        offers = []
        for id, obj in self.offer_map.items():
            offers.append(obj)
        return offers