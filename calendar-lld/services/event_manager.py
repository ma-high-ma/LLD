from models.event import Event
from services.calendar_manager import CalendarManagerService


class EventManager:
    """
    Event -> Calendar -> UserCalendar -> User

    """
    def create_event(self, id, name, day, start_time, end_time, members, check_availability=False):
        event = Event(id, name, day, start_time, end_time, members)

        # Add event to calendars of all the members
        for user_id in members:
            if check_availability and not CalendarManagerService().is_user_available(user_id, day, start_time, end_time):
                print(user_id, " not Available. Event Creation Failed.")
                return
            calendar = CalendarManagerService().get_calendar(user_id=user_id)
            if not calendar.day_wise_events.get(day):
                calendar.day_wise_events[day] = []
            self.add_event(event, calendar, day)

        return event

    def add_event(self, event, calendar, day):
        events = calendar.day_wise_events[day] + [event]
        events.sort(key=lambda x: x.time_slot.start_time)
        calendar.day_wise_events[day] = events
