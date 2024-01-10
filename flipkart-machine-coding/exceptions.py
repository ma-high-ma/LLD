class InterviewNotFound(Exception):
    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        message = f"interview with ID = {self.id} NOT found"
        return message


class InterviewerNotFound(Exception):
    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        message = f"interviewer with ID = {self.id} NOT found"
        return message


class IntervieweeNotFound(Exception):
    def __init__(self, id=None):
        self.id = id

    def __str__(self):
        message = f"interviewee with ID = {self.id} NOT found"
        return message
