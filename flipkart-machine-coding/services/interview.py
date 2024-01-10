from constants import RoundType, IntervieweeStatus, InterviewerStatus
from dao.interview import InterviewDao
from services.interviewee import IntervieweeService
from services.interviewer import InterviewerService


class InterviewService:
    def create(self, interviewer_id, interviewee_id, type, slot):
        return InterviewDao().create(interviewer_id, interviewee_id, type, slot)

    def allocate(self, algo="key1"):
        """
        rounds = [MC, MC, PSDS]
        get all interviewees
        for each interviewee
            for each round
                get all interviewers status = available
                if any interview with same interviewee_id + interviewer_id -> continue
                if round_type in interviewer_types
                    sort each of the slots
                    if interviewee_slot in interviewer slot
                        create interview
                        remove available slots
                        update status of interviewer
                if interview not created:
                    print message

        """
        rounds = [RoundType.MACHINE_CODING, RoundType.MACHINE_CODING, RoundType.PSDS, RoundType.PSDS]
        interviews_created = []
        interviewees = IntervieweeService().get_by_status(status=IntervieweeStatus.NOT_STARTED)
        for interviewee_obj in interviewees:

            interviewee_obj.status = IntervieweeStatus.IN_PROGRESS
            for round in rounds:
                interviewer, slot = self.get_interviewer_and_slot(interviewee_obj=interviewee_obj, round_type=round)
                if not interviewer:
                    message = f"CandidateId {interviewee_obj.id} Round: {round} -> Not possible"
                    print(message)
                    continue
                interview = self.create(interviewer_id=interviewer.id, interviewee_id=interviewee_obj.id, slot=slot,
                                        type=round)
                InterviewerService().remove_availability(id=interviewer.id, slot=slot)
                IntervieweeService().remove_availability(id=interviewee_obj.id, slot=slot)
                interviews_created.append(interview)
            if len(interviews_created) == 3:
                interviewee_obj.status = IntervieweeStatus.COMPLETED

    def get_all(self):
        return InterviewDao().get_all()

    def view_all_interviews(self):
        interviews = self.get_all()
        if not interviews:
            print("No Interviews")
        self.print_interviews(interviews)

    def print_interviews(self, interview_objs):
        for obj in interview_objs:
            message = f"Interview ID: {obj.id} InterviewerID: {obj.interviewer_id} IntervieweeID: {obj.interviewee_id} Round Type: {obj.type} Slot: {obj.slot}"
            print(message)

    def get_existing_interviews(self, interviewer_id, interviewee_id):
        interviews = self.get_all()
        for interview in interviews:
            if interview.interviewer_id == interviewer_id and interview.interviewee_id == interviewee_id:
                return interview
        return None

    def can_allocate(self, interviewer_obj, interviewee_obj):
        is_existing_interview = self.get_existing_interviews(interviewer_id=interviewer_obj.id,
                                                             interviewee_id=interviewee_obj.id)
        if is_existing_interview:
            return False
        return True

    def get_available_slot(self, interviewee_slots, interviewer_slots):
        for interviewee_slot in interviewee_slots:
            if interviewee_slot in interviewer_slots:
                return interviewee_slot
        return None

    def get_interviewer_and_slot(self, interviewee_obj, round_type):
        interviewers = self.get_interviewers()
        for interviewer_obj in interviewers:
            if self.can_allocate(interviewer_obj=interviewer_obj, interviewee_obj=interviewee_obj):
                slot = self.get_available_slot(interviewee_slots=interviewee_obj.available_slots,
                                               interviewer_slots=interviewer_obj.available_slots)
                if slot:
                    return interviewer_obj, slot
        return None, None

    def get_interviewers(self, key="key1"):
        interviewer_class = InteriewerClass().get_obj(key="abc")
        interviewer_class().get_interviewers()

        # interviewer getting startegy in "runtime"
        base class
        concrete class(base class)

