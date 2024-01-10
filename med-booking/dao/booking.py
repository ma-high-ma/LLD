from constants import BookingStatus
from exceptions import DoctorNotFound
import uuid

from models.booking import Booking


class BookingDAO:
    booking_map = {}

    def create(self, patient_id, doctor_id, slot_id, status=BookingStatus.ACTIVE):
        booking = Booking(id=uuid.uuid4(), patient_id=patient_id, doctor_id=doctor_id, time_slot_id=slot_id, status=status)
        self.booking_map[booking.id] = booking
        return booking

    def get_by_id(self, id):
        try:
            return self.booking_map[id]
        except KeyError:
            raise DoctorNotFound(id)

    def get_all(self):
        bookings = []
        for b_id, obj in self.booking_map.items():
            bookings.append(obj)
        return bookings
