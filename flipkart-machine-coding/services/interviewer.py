from constants import InterviewerStatus
from dao.interviewer import InterviewerDao
from exceptions import InterviewerNotFound


class InterviewerService:
    def regsiter(self, id, name, experience, slots, types):
        interviewer = InterviewerDao().create(id=id, name=name, slots=slots, experience=experience, types=types)
        return interviewer

    def get_by_type_and_status(self, status, type, ordered=False):
        interviewers = InterviewerDao().get_by_type_and_status(status=status, type=type)
        if not ordered:
            return interviewers
        interviewers.sort(reverse=True, key=lambda x: len(x.available_slots))
        return interviewers

    def remove_availability(self, id, slot):
        try:
            interviewer = InterviewerDao().get_by_id(id=id)
            interviewer.available_slots.remove(slot)
            if len(interviewer.available_slots) == 0:
                interviewer.status = InterviewerStatus.BOOKED
        except InterviewerNotFound as e:
            print("Error: ", str(e))
