from dao.time_slot import TimeSlotDAO


class AvailabilityService:
    availability_map = {}
    """
    {
        speciality: {
            doctor_id: [slot_id1, slot_id2]
        }
    }
    """

    def add_availability(self, doctor_obj, slot_id):
        if not doctor_obj:
            return False
        if not self.availability_map.get(doctor_obj.speciality):
            self.availability_map[doctor_obj.speciality] = {}
        if not self.availability_map[doctor_obj.speciality].get(doctor_obj.id):
            self.availability_map[doctor_obj.speciality][doctor_obj.id] = []
        doctor_availability = self.availability_map[doctor_obj.speciality][doctor_obj.id]
        if slot_id not in doctor_availability:
            self.availability_map[doctor_obj.speciality][doctor_obj.id].append(slot_id)
        return True

    def remove_availability(self, doctor_id, speciality, slot_id):
        self.availability_map[speciality][doctor_id].remove(slot_id)


    def get_available_slots_by_doctor_id(self, doctor_id, speciality):
        return self.availability_map[speciality].get(doctor_id, [])


    def get_slots_by_speciality(self, speciality):
        available_doctors = self.availability_map[speciality]
        slots_doctor = []
        for doctor_id in available_doctors:
            for slot_id in available_doctors[doctor_id]:
                slot_obj = TimeSlotDAO().get_by_id(slot_id=slot_id)
                slots_doctor.append([slot_obj, doctor_id])

        slots_doctor.sort(key=lambda x: x[0].start_time)
        return slots_doctor




