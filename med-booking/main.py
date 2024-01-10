from constants import Speciality
from services.booking import BookingService
from services.doctor import DoctorService
from services.patient import PatientService

if __name__ == '__main__':
    doctor = DoctorService().register(name="Curious", speciality=Speciality.CARDIOLOGIST)
    doctor2 = DoctorService().register(name="Dermat", speciality=Speciality.DERMAT)
    DoctorService().register_availability(doctor_id=doctor.id, start_time=900, end_time=930)
    DoctorService().register_availability(doctor_id=doctor.id, start_time=1000, end_time=1030)
    DoctorService().register_availability(doctor_id=doctor.id, start_time=1100, end_time=1130)
    DoctorService().register_availability(doctor_id=doctor2.id, start_time=1100, end_time=1130)
    patient = PatientService().register(name="patient1")
    patient2 = PatientService().register(name="patient2")
    DoctorService().get_slots_by_speciality(speciality=Speciality.CARDIOLOGIST)
    BookingService().book(patient_id=patient.id, doctor_id=doctor.id, start_time=1000, end_time=1030)
    DoctorService().get_slots_by_speciality(speciality=Speciality.CARDIOLOGIST)
    BookingService().get_bookings_by_doctor_id(doctor_id=doctor.id)

    BookingService().book(patient_id=patient2.id, doctor_id=doctor.id, start_time=1100, end_time=1130)
    BookingService().book(patient_id=patient2.id, doctor_id=doctor2.id, start_time=1100, end_time=1130)
    BookingService().book(patient_id=patient2.id, doctor_id=doctor.id, start_time=1000, end_time=1030)


