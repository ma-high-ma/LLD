class PatientNotFound(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Patient with id {self.id} Not Found"


class BookingNotFound(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Booking with id {self.id} Not Found"


class DoctorNotFound(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Doctor with id {self.id} Not Found"
