import uuid

from exceptions import InterviewNotFound
from models.interview import Interview


class InterviewDao:
    interview_map = {}
    # {1234: obj}

    def create(self, interviewer_id, interviewee_id, type, slot):
        interview_id = uuid.uuid4()
        interview = Interview(id=interview_id, interviewer_id=interviewer_id, interviewee_id=interviewee_id, type=type, slot=slot)
        self.interview_map[interview_id] = interview
        return interview

    def get_by_id(self, id):
        try:
            return self.interview_map[id]
        except KeyError:
            raise InterviewNotFound(id=id)

    def get_all(self):
        interviews = []
        for id, obj in self.interview_map.items():
            interviews.append(obj)
        return interviews

