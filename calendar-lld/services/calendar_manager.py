from models.calendar import Calendar
from models.user_calendar import UserCalendar


class CalendarManagerService:

    """
    userCalendarMap = {
        user_calendar_id: <userCalendarObj>
    }
    """

    userCalendarMap = {}
    calendarMap = {}

    def create_calendar(self, user_id, calendar_id, name):
        calendar = Calendar(id=calendar_id, name=name)
        self.calendarMap[calendar.id] = calendar
        id = f"{user_id}-{calendar_id}"
        user_calendar = UserCalendar(id=id, user_id=user_id, calendar_id=calendar_id)
        self.userCalendarMap[user_calendar.id] = user_calendar
        return calendar

    def get_calendar(self, user_id):
        for k, v in self.userCalendarMap.items():
            if v.user_id == user_id:
                return self.calendarMap[v.calendar_id]
        return None

    def get_user_events_by_day(self, user_id, day):
        calendar = self.get_calendar(user_id=user_id)
        user_events_by_day = calendar.day_wise_events
        events = user_events_by_day.get(day)
        return events

    def is_user_available(self, user_id, day, start_time, end_time):
        events = self.get_user_events_by_day(user_id=user_id, day=day)
        if not events:
            # No events on this day
            return True
        available_slots = self.get_available_slots(user_id=user_id, day=day, start_time=start_time, end_time=end_time)
        for s, e in available_slots:
            if s <= start_time and e >= end_time:
                return True
        return False

    def get_available_slots(self, user_id, day, start_time=7, end_time=18, display=False):
        events = self.get_user_events_by_day(user_id=user_id, day=day) or []

        occupied_slots = self.get_slots_from_objs(events)
        available_slots = self.__get_available_slots(occupied_slots=occupied_slots, start=start_time, end=end_time)
        if display:
            self.print_available_slots(user_id=user_id, day=day, slots=available_slots)
        return available_slots

    def __get_available_slots(self, occupied_slots, start, end):
        available_slots = []
        curr = start
        for s, e in occupied_slots:
            if curr > end:
                break
            if curr < s:
                available_slots.append([curr, s])
            curr = max(curr, e)
        if curr < end:
            available_slots.append([curr, end])
        return available_slots

    def print_available_slots(self, user_id, day, slots):
        print("Available slots for ", user_id, " on ", day, "-")
        for start, end in slots:
            print(start, " to ", end)
        print()

    def get_slots_from_objs(self, events):
        slots = [[x.time_slot.start_time, x.time_slot.end_time] for x in events]
        return slots

    def print_user_events(self, user_id, day):
        print("Events of ", user_id, " on ", day, " : ")
        events = self.get_user_events_by_day(user_id, day)
        if not events:
            print("No Events")
            return
        for e in events:
            print("ID: ", e.id, "Name: ", e.name, "Time : ", e.time_slot.start_time, " - ", e.time_slot.end_time)
        print()

    def get_conflicting_slots(self, user_id, day):
        print("Conflicting Events of ", user_id, " - ")
        events = self.get_user_events_by_day(user_id, day)

        if not events:
            print("There are no events")
            return

        is_conflicting = False
        prev = events[0]
        for i in range(1, len(events)):
            curr = events[i]
            curr_start, curr_end = curr.time_slot.start_time, curr.time_slot.end_time
            prev_start, prev_end = prev.time_slot.start_time, prev.time_slot.end_time

            if curr_start > prev_start:
                if curr_end <= prev_end:
                    print(prev.id, " has conflict with ", curr.id)
                    is_conflicting = True
            prev = curr

        if not is_conflicting:
            print("No conflicting events")
        print()
        return
