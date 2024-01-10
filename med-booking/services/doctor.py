from dao.doctor import DoctorDAO
from dao.time_slot import TimeSlotDAO
from exceptions import DoctorNotFound
from services.availability import AvailabilityService


class DoctorService:
    def register(self, name, speciality):
        doctor = DoctorDAO().create(name, speciality)
        return doctor

    def register_availability(self, doctor_id, start_time, end_time):
        slot = TimeSlotDAO().get_or_create(start_time, end_time)
        doctor = DoctorService().get_by_id(id=doctor_id)
        added = AvailabilityService().add_availability(doctor_obj=doctor, slot_id=slot.id)
        return added

    def get_by_id(self, id):
        try:
            return DoctorDAO().get_by_id(id=id)
        except DoctorNotFound:
            return None

    def is_available(self, doctor_id, slot_id):
        doctor = self.get_by_id(doctor_id)
        # If doctor not present
        available_slots = AvailabilityService().get_available_slots_by_doctor_id(doctor_id=doctor_id, speciality=doctor.speciality)
        if slot_id in available_slots:
            return True
        return False

    def get_slots_by_speciality(self, speciality):
        slots_doctor = AvailabilityService().get_slots_by_speciality(speciality=speciality)

        for slot_obj, doctor_id in slots_doctor:
            doctor = DoctorService().get_by_id(doctor_id)
            message = f"{doctor.name} ({slot_obj.start_time} - {slot_obj.end_time})"
            print(message)

    def remove_availability(self, doctor_id, slot_id):
        doctor = self.get_by_id(doctor_id)
        AvailabilityService().remove_availability(doctor_id=doctor_id, slot_id=slot_id, speciality=doctor.speciality)

    def add_availability(self, doctor_id, slot_id):
        doctor = self.get_by_id(doctor_id)
        AvailabilityService().add_availability(doctor_obj=doctor, slot_id=slot_id)
