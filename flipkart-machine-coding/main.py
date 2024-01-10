from constants import RoundType
from services.interview import InterviewService
from services.interviewee import IntervieweeService
from services.interviewer import InterviewerService

if __name__ == '__main__':
    interviewer1 = InterviewerService().regsiter(id="IN1", name="int1", slots=[1,2,3,4], types=[RoundType.MACHINE_CODING, RoundType.PSDS], experience=7)
    interviewer2 = InterviewerService().regsiter(id="IN2", name="int2", slots=[1,2,3,4,7], types=[RoundType.MACHINE_CODING, RoundType.PSDS], experience=7)
    interviewer3 = InterviewerService().regsiter(id="IN3", name="int3", slots=[1,2,7,8], types=[RoundType.MACHINE_CODING, RoundType.PSDS], experience=7)

    candidate3 = IntervieweeService().regsiter(id="CAN3", name="can3", slots=[7, 8])
    candidate1 = IntervieweeService().regsiter(id="CAN1", name="can1", slots=[1, 2, 3, 7, 8])
    candidate2 = IntervieweeService().regsiter(id="CAN2", name="can2", slots=[1, 2, 3, 7, 8])

    InterviewService().allocate()

    InterviewService().view_all_interviews()
