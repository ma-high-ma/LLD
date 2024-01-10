from exceptions import PatientNotFound
from models.patient import Patient
import uuid


class PatientDAO:
    patient_map = {}

    def create(self, name):
        patient = Patient(id=uuid.uuid4(), name=name)
        self.patient_map[patient.id] = patient
        return patient

    def get_by_id(self, id):
        try:
            return self.patient_map[id]
        except KeyError:
            raise PatientNotFound(id)
