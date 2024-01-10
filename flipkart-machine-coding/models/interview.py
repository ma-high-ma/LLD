from constants import InterviewStatus


class Interview:
    def __init__(self, id, interviewer_id, interviewee_id, type, slot, status=InterviewStatus.SCHEDULED):
        self.id = id
        self.interviewer_id = interviewer_id
        self.interviewee_id = interviewee_id
        self.type = type
        self.slot = slot
        self.status = status
