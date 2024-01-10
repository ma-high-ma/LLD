from dao.interviewee import IntervieweeDao
from exceptions import IntervieweeNotFound


class IntervieweeService:
    def regsiter(self, id, name, slots):
        interviewee = IntervieweeDao().create(id=id, name=name, slots=slots)
        return interviewee

    def get_by_status(self, status):
        return IntervieweeDao().get_by_status(status=status)

    def remove_availability(self, id, slot):
        try:
            interviewee = IntervieweeDao().get_by_id(id=id)
            interviewee.available_slots.remove(slot)
        except IntervieweeNotFound as e:
            print("Error: ", str(e))

    def update_status(self, id, status):
        interviewee = IntervieweeDao().get_by_id(id=id)
        interviewee.status = status
