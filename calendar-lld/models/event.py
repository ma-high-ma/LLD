from models.timeslot import TimeSlot


class Event:
    def __init__(self, id, name, day, start_time, end_time, members):
        self.id = id
        self.time_slot = TimeSlot(start_time, end_time)
        self.day = day
        self.members = members
        self.name=name
