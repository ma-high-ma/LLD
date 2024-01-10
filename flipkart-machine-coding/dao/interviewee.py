from constants import IntervieweeStatus
from exceptions import IntervieweeNotFound
from models.interviewee import Interviewee


class IntervieweeDao:
    interviewee_map = {}

    def create(self, id, name, slots):
        interviewee = Interviewee(id=id, name=name, available_slots=slots, status=IntervieweeStatus.NOT_STARTED)
        self.interviewee_map[interviewee.id] = interviewee
        return interviewee

    def get_by_id(self, id):
        try:
            return self.interviewee_map[id]
        except KeyError:
            raise IntervieweeNotFound(id=id)

    def get_by_status(self, status):
        interviewees = []
        for id, obj in self.interviewee_map.items():
            if obj.status == status:
                interviewees.append(obj)

        return interviewees
