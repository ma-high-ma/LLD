class Calendar:
    def __init__(self, id, name, day_wise_events=None):
        self.id = id
        self.name = name
        self.day_wise_events = day_wise_events if day_wise_events else {}
