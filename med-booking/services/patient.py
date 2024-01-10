from dao.patient import PatientDAO


class PatientService:
    def register(self, name):
        patient = PatientDAO().create(name)
        return patient
