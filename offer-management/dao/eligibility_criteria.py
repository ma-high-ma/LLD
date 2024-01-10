import uuid

from models.eligibility_criteria import EligibilityCriteria


class EligibilityCriteriaDao:
    eligibility_criteria_map = {}

    def create(self, entity, key, value, condition):
        eligibility_criteria_id = uuid.uuid4()
        eligibility_criteria = EligibilityCriteria(id=eligibility_criteria_id, entity=entity, key=key, value=value, condition=condition)
        self.eligibility_criteria_map[eligibility_criteria_id] = eligibility_criteria
        return eligibility_criteria