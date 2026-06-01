class Patient:
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
class Doctor:
    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
class Appointment:
    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor
    def get_details(self):
        print("      Appointment      ")
        print("Patient:", self.patient.name)
        print("Age:", self.patient.age)
        print("Diagnosis:", self.patient.diagnosis)
        print("Doctor:", self.doctor.name)
        print("Specialisation:", self.doctor.specialisation)
patient1 = Patient("Rahees", 20, "Fever")
doctor1 = Doctor("Dr Thoha Ashraf", "General Medicine")
appointment1 = Appointment(patient1, doctor1)
appointment1.get_details()