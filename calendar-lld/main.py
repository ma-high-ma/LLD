from services.calendar_manager import CalendarManagerService
from services.event_manager import EventManager
from services.helpers.time import TimeHelper
from services.user_manager import UserManagerService

if __name__ == '__main__':
    """
    Calendar App
    - Create user:  Done
    - Create calendar: Done
    - Create event: Done
    - Get events for a user in a day (w/ start and end time) Done
    - Find available slots in a day (w/ start and end time): Done
    - get conflicting slots in a day Done
    Optional
    - Attach room to an event
    - Create team
    - Assign event to a team
    """

    u0 = UserManagerService().create_user(id="u0", name="User0")
    u1 = UserManagerService().create_user(id="u1", name="User0")
    u2 = UserManagerService().create_user(id="u2", name="User0")

    c0 = CalendarManagerService().create_calendar(calendar_id="c0", user_id=u0.id, name="personal")
    c1 = CalendarManagerService().create_calendar(calendar_id="c1", user_id=u1.id, name="personal")
    c2 = CalendarManagerService().create_calendar(calendar_id="c2", user_id=u2.id, name="personal")

    e0 = EventManager().create_event(id="e0", name="Sync call 1", day="10102023", start_time=12, end_time=13, members=[u1.id, u2.id])
    e1 = EventManager().create_event(id="e1", name="Sync call 2", day="10102023", start_time=11, end_time=15, members=[u1.id, u0.id])
    e2 = EventManager().create_event(id="e2", name="Sync call 3", day="10102023", start_time=9, end_time=10, members=[u1.id, u0.id])
    e3 = EventManager().create_event(id="e3", name="Sync call 4", day="10102023", start_time=17, end_time=19, members=[u1.id, u0.id])
    e4 = EventManager().create_event(id="e4", name="Sync call 5", day="10102023", start_time=10, end_time=12, members=[u1.id, u0.id], check_availability=True)

    CalendarManagerService().print_user_events(user_id=u0.id, day='10102023')
    CalendarManagerService().print_user_events(user_id=u1.id, day='10102023')
    CalendarManagerService().print_user_events(user_id=u2.id, day='10102023')

    CalendarManagerService().get_available_slots(user_id=u1.id, day="10102023", display=True)
    CalendarManagerService().get_available_slots(user_id=u1.id, day="10102023", display=True, start_time=9, end_time=14)
    CalendarManagerService().get_available_slots(user_id=u1.id, day="10102022", display=True)

    CalendarManagerService().get_conflicting_slots(user_id=u1.id, day="10102023")
    CalendarManagerService().get_conflicting_slots(user_id=u0.id, day="10102023")
    CalendarManagerService().get_conflicting_slots(user_id=u1.id, day="10112023")

    print(TimeHelper().get_time_in_int("2:30"))
    print(TimeHelper().get_time_in_str(1430))
