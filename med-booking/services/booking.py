from constants import BookingStatus
from dao.booking import BookingDAO
from dao.time_slot import TimeSlotDAO
from dao.wait_list import WaitListDao
from exceptions import BookingNotFound
from services.doctor import DoctorService


class BookingService:

    def book(self, patient_id, doctor_id, start_time=None, end_time=None, slot_id=None):
        if not slot_id:
            slot = TimeSlotDAO().get_slot_obj(start_time=start_time, end_time=end_time)
            slot_id = slot.id
        is_doctor_available = DoctorService().is_available(doctor_id=doctor_id, slot_id=slot_id)
        is_patient_available = self.is_patient_available(patient_id, slot_id)
        if is_doctor_available and is_patient_available:
            DoctorService().remove_availability(doctor_id=doctor_id, slot_id=slot_id)
            booking = BookingDAO().create(patient_id=patient_id, doctor_id=doctor_id, slot_id=slot_id)
            self.print_bookings([booking])
            return booking
        elif not is_doctor_available:
            WaitListDao().add_to_waitlist(doctor_id, patient_id, slot_id)
            print("Doctor unavailable")
            return None
        elif not is_patient_available:
            print("Patient unavailable")
            return None

    def cancel(self, booking_id):
        try:
            booking = BookingDAO().get_by_id(id=booking_id)
        except BookingNotFound as e:
            print(str(e))
            return
        booking.status = BookingStatus.CANCELLED
        print("booking cancelled id = ", booking_id)
        doctor_id = booking.doctor_id
        # check waitlist
        # if patient present -> create new booking
        patient_id = self.get_waitlisted_patient(doctor_id, booking.time_slot_id)
        DoctorService().add_availability(doctor_id=doctor_id, slot_id=booking.time_slot_id)
        if patient_id:
            booking = self.book(patient_id=patient_id, doctor_id=doctor_id, slot_id=booking.time_slot_id)


    def get_waitlisted_patient(self, doctor_id, slot_id):
        patient_id = WaitListDao().get_and_remove_patient_id_from_waitlist(doctor_id, slot_id)
        return patient_id

    def get_bookings_by_doctor_id(self, doctor_id):
        bookings = BookingDAO().get_all()
        doctor_bookings = []
        for booking in bookings:
            if booking.doctor_id == doctor_id:
                doctor_bookings.append(booking)
        self.print_bookings(doctor_bookings)
        return doctor_bookings

    def print_bookings(self, booking_objs):
        for booking in booking_objs:
            slot_obj = TimeSlotDAO().get_by_id(booking.time_slot_id)
            message = f"Doctor ID: {booking.doctor_id} Patient: {booking.patient_id} Start: {slot_obj.start_time} End: {slot_obj.end_time}"
            print(message)

    def is_patient_available(self, patient_id, slot_id):
        bookings = BookingDAO().get_all()
        for booking in bookings:
            if booking.patient_id == patient_id and booking.time_slot_id == slot_id:
                return False
        return True
