class WaitListDao:
    waitlist_map = {}
    """
    {
        doctor_id_slot_id : []
    }
    """
    def add_to_waitlist(self, doctor_id, patient_id, slot_id):
        key = self.get_key(doctor_id, slot_id)
        if not self.waitlist_map.get(key):
            self.waitlist_map[key] = []
        self.waitlist_map[key].append(patient_id)
        print(patient_id, "added to waitlist")

    def get_and_remove_patient_id_from_waitlist(self, doctor_id, slot_id):
        key = self.get_key(doctor_id, slot_id)
        if not self.waitlist_map.get(key):
            return None
        return self.waitlist_map[key].pop(0)

    def get_key(self, doctor_id, slot_id):
        return f"{doctor_id}_{slot_id}"
