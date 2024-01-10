import uuid

from models.time_slot import TimeSlot


class TimeSlotDAO:
    time_slot_map = {}

    def get_or_create(self, start_time, end_time):
        slot_obj = self.get_slot_obj(start_time, end_time)
        if not slot_obj:
            slot_obj = TimeSlot(id=uuid.uuid4(), start_time=start_time, end_time=end_time)
            self.time_slot_map[slot_obj.id] = slot_obj
        return slot_obj

    def get_slot_obj(self, start_time, end_time):
        for id, slot_obj in self.time_slot_map.items():
            if slot_obj.start_time == start_time:
                return slot_obj
        return None

    def get_by_id(self, slot_id):
        return self.time_slot_map.get(slot_id)
