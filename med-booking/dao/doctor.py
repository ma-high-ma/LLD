from exceptions import DoctorNotFound
import uuid

from models.doctor import Doctor


class DoctorDAO:
    doctor_map = {}

    def create(self, name, speciality):
        doctor = Doctor(id=uuid.uuid4(), name=name, speciality=speciality)
        self.doctor_map[doctor.id] = doctor
        return doctor

    def get_by_id(self, id):
        try:
            return self.doctor_map[id]
        except KeyError:
            raise DoctorNotFound(id)
