from constants import InterviewerStatus
from exceptions import InterviewerNotFound
from models.interviewer import Interviewer


class InterviewerDao:
    interviewer_map = {}

    def create(self, id, name, slots, experience, types):
        status = self.__get_status(slots=slots)
        interviewer = Interviewer(id=id, name=name, available_slots=slots, experience=experience, types=types, status=status)
        self.interviewer_map[interviewer.id] = interviewer
        return interviewer

    def get_by_id(self, id):
        try:
            return self.interviewer_map[id]
        except KeyError:
            raise InterviewerNotFound(id=id)

    def __get_status(self, slots):
        if len(slots) == 0:
            return InterviewerStatus.BOOKED
        else:
            return InterviewerStatus.AVAILABLE

    def get_by_status(self, status):
        interviewers = []
        for id, obj in self.interviewer_map.items():
            if obj.status == status:
                interviewers.append(obj)

        return interviewers

    def get_by_type_and_status(self, status, type):
        interviewers = self.get_by_status(status=status)
        eligible_interviewers = []
        for interviewer in interviewers:
            if type in interviewer.types:
                eligible_interviewers.append(interviewer)
        return eligible_interviewers
