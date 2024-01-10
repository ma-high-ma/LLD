class Booking:
    def __init__(self, id, patient_id, doctor_id, time_slot_id, status):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.time_slot_id = time_slot_id
        self.status = status