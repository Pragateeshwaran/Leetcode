from datetime import datetime, date
from typing import List, Optional

# --- 1. User Hierarchy ---
class User:
    """Abstract base class for all system users."""
    def __init__(self, user_id: str, username: str, password: str, contact_info: str):
        self.__user_id = user_id
        self.__username = username
        self.__password = password # In a real system, hash passwords!
        self.__contact_info = contact_info

    def get_user_id(self) -> str:
        return self.__user_id

    def get_username(self) -> str:
        return self.__username

    def get_contact_info(self) -> str:
        return self.__contact_info

    def login(self, password: str) -> bool:
        """Simulates user login."""
        return self.__password == password # Basic check
        # In production: use bcrypt, compare hashed passwords

    def logout(self):
        print(f"{self.__username} logged out.")

    def update_profile(self, new_contact_info: str):
        self.__contact_info = new_contact_info
        print(f"Profile for {self.__username} updated.")

    def display_user_info(self):
        print(f"User ID: {self.__user_id}, Username: {self.__username}, Contact: {self.__contact_info}")


class Patient(User):
    """Represents a patient in the hospital system."""
    def __init__(self, user_id: str, username: str, password: str, contact_info: str,
                 date_of_birth: date, gender: str):
        super().__init__(user_id, username, password, contact_info)
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__medical_record: Optional[MedicalRecord] = None # One-to-one relationship
        self.__appointments: List[Appointment] = [] # One-to-many
        self.__invoices: List[Invoice] = [] # One-to-many
        self.__feedbacks: List[Feedback] = [] # One-to-many

    def get_date_of_birth(self) -> date:
        return self.__date_of_birth

    def get_gender(self) -> str:
        return self.__gender

    def set_medical_record(self, record: 'MedicalRecord'):
        self.__medical_record = record

    def get_medical_record(self) -> Optional['MedicalRecord']:
        return self.__medical_record

    def add_appointment(self, appointment: 'Appointment'):
        self.__appointments.append(appointment)

    def book_appointment(self, doctor: 'Doctor', appt_datetime: datetime, appt_type: str) -> 'Appointment':
        new_appt = Appointment(f"APT{len(self.__appointments) + 1}", appt_datetime, "Scheduled", appt_type, self, doctor)
        self.__appointments.append(new_appt)
        doctor.add_appointment(new_appt) # Add to doctor's list too
        print(f"{self.get_username()} booked an appointment with Dr. {doctor.get_username()} on {appt_datetime}.")
        return new_appt

    def view_medical_record(self):
        if self.__medical_record:
            print(f"\n--- Medical Record for {self.get_username()} ---")
            self.__medical_record.display_record()
        else:
            print(f"No medical record found for {self.get_username()}.")

    def add_invoice(self, invoice: 'Invoice'):
        self.__invoices.append(invoice)

    def make_payment(self, invoice: 'Invoice', amount: float, method: str) -> 'Payment':
        payment = Payment(f"PAY{len(invoice.get_payments()) + 1}", datetime.now(), amount, method)
        invoice.add_payment(payment)
        print(f"{self.get_username()} made a payment of ${amount} for Invoice {invoice.get_invoice_id()} via {method}.")
        return payment

    def give_feedback(self, service: 'HospitalService', rating: int, comment: str):
        feedback = Feedback(f"FB{len(self.__feedbacks) + 1}", rating, comment, datetime.now(), self, service)
        self.__feedbacks.append(feedback)
        service.add_feedback(feedback)
        print(f"{self.get_username()} gave {rating} stars for {service.get_name()}.")
        return feedback

class Doctor(User):
    """Represents a doctor in the hospital system."""
    def __init__(self, user_id: str, username: str, password: str, contact_info: str,
                 specialization: str, license_number: str):
        super().__init__(user_id, username, password, contact_info)
        self.__specialization = specialization
        self.__license_number = license_number
        self.__availability: List[datetime] = [] # Example: list of available slots
        self.__appointments: List[Appointment] = [] # One-to-many
        self.__prescriptions: List[Prescription] = [] # One-to-many

    def get_specialization(self) -> str:
        return self.__specialization

    def add_appointment(self, appointment: 'Appointment'):
        self.__appointments.append(appointment)

    def manage_availability(self, new_slot: datetime):
        self.__availability.append(new_slot)
        print(f"Dr. {self.get_username()}'s availability updated with slot: {new_slot}.")

    def approve_reject_appointment(self, appointment: 'Appointment', status: str):
        if appointment in self.__appointments:
            appointment.set_status(status)
            print(f"Dr. {self.get_username()} {status} appointment {appointment.get_appointment_id()}.")
        else:
            print("Appointment not found or not associated with this doctor.")

    def access_patient_history(self, patient: Patient):
        if patient.get_medical_record():
            patient.view_medical_record()
        else:
            print(f"No medical record available for {patient.get_username()}.")

    def prescribe_medication(self, patient: Patient, items: List['PrescriptionItem'], instructions: str) -> 'Prescription':
        prescription = Prescription(f"PRX{len(self.__prescriptions) + 1}", datetime.now(), instructions, self, patient)
        for item in items:
            prescription.add_item(item)
        self.__prescriptions.append(prescription)
        patient.get_medical_record().add_prescription(prescription) # Link to patient's medical record
        print(f"Dr. {self.get_username()} prescribed medication to {patient.get_username()}.")
        return prescription

# --- Other User Roles (simplified for brevity) ---
class Nurse(User):
    def __init__(self, user_id, username, password, contact_info, department: str):
        super().__init__(user_id, username, password, contact_info)
        self.__department = department

class Admin(User):
    def __init__(self, user_id, username, password, contact_info):
        super().__init__(user_id, username, password, contact_info)

class Pharmacist(User):
    def __init__(self, user_id, username, password, contact_info, pharmacy: 'Pharmacy'):
        super().__init__(user_id, username, password, contact_info)
        self.__pharmacy = pharmacy # Association
    
    def manage_stock_levels(self, medication: 'Medication', new_stock: int):
        medication.set_stock_level(new_stock)
        print(f"{self.get_username()} updated stock for {medication.get_name()} to {new_stock}.")

class LabTechnician(User):
    def __init__(self, user_id, username, password, contact_info, lab_specialty: str):
        super().__init__(user_id, username, password, contact_info)
        self.__lab_specialty = lab_specialty


# --- 2. Appointment ---
class Appointment:
    def __init__(self, appt_id: str, date_time: datetime, status: str, appt_type: str,
                 patient: Patient, doctor: Doctor):
        self.__appointment_id = appt_id
        self.__date_time = date_time
        self.__status = status # e.g., "Scheduled", "Confirmed", "Cancelled", "Completed"
        self.__type = appt_type
        self.__patient = patient # Association: Patient books Appointment
        self.__doctor = doctor   # Association: Doctor handles Appointment

    def get_appointment_id(self) -> str:
        return self.__appointment_id

    def get_date_time(self) -> datetime:
        return self.__date_time

    def get_status(self) -> str:
        return self.__status

    def set_status(self, new_status: str):
        self.__status = new_status

    def get_patient(self) -> Patient:
        return self.__patient

    def get_doctor(self) -> Doctor:
        return self.__doctor

    def get_details(self):
        return {
            "id": self.__appointment_id,
            "datetime": self.__date_time,
            "status": self.__status,
            "type": self.__type,
            "patient": self.__patient.get_username(),
            "doctor": self.__doctor.get_username()
        }

# --- 3. Patient Medical Records ---
class MedicalRecord:
    def __init__(self, record_id: str, patient: Patient):
        self.__record_id = record_id
        self.__patient = patient # Association: MedicalRecord belongs to one Patient
        self.__date_created = datetime.now()
        self.__last_updated = datetime.now()
        self.__diagnoses: List[str] = []
        self.__treatments: List[str] = []
        self.__allergies: List[str] = []
        self.__prescriptions: List[Prescription] = [] # Association: MedicalRecord contains Prescriptions

    def get_record_id(self) -> str:
        return self.__record_id

    def add_diagnosis(self, diagnosis: str):
        self.__diagnoses.append(diagnosis)
        self.__last_updated = datetime.now()

    def add_treatment(self, treatment: str):
        self.__treatments.append(treatment)
        self.__last_updated = datetime.now()

    def add_allergy(self, allergy: str):
        self.__allergies.append(allergy)
        self.__last_updated = datetime.now()

    def add_prescription(self, prescription: 'Prescription'):
        self.__prescriptions.append(prescription)
        self.__last_updated = datetime.now()

    def display_record(self):
        print(f"Record ID: {self.__record_id}")
        print(f"Patient: {self.__patient.get_username()}")
        print(f"Created: {self.__date_created}, Last Updated: {self.__last_updated}")
        print(f"Diagnoses: {', '.join(self.__diagnoses) if self.__diagnoses else 'None'}")
        print(f"Treatments: {', '.join(self.__treatments) if self.__treatments else 'None'}")
        print(f"Allergies: {', '.join(self.__allergies) if self.__allergies else 'None'}")
        print("Prescriptions:")
        if self.__prescriptions:
            for prx in self.__prescriptions:
                prx.display_prescription()
        else:
            print("  No prescriptions.")

# --- 4. Pharmacy & Prescription Management ---
class Medication:
    def __init__(self, med_id: str, name: str, description: str, price: float, expiration_date: date, stock_level: int):
        self.__medication_id = med_id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__expiration_date = expiration_date
        self.__stock_level = stock_level

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock_level(self) -> int:
        return self.__stock_level

    def set_stock_level(self, new_level: int):
        self.__stock_level = new_level

    def display_medication_info(self):
        print(f"  Medication: {self.__name} (ID: {self.__medication_id})")
        print(f"  Description: {self.__description}")
        print(f"  Price: ${self.__price:.2f}, Stock: {self.__stock_level}, Expires: {self.__expiration_date}")

class PrescriptionItem:
    def __init__(self, medication: Medication, dosage: str, frequency: str, quantity: int):
        self.__medication = medication # Association: Refers to one Medication
        self.__dosage = dosage
        self.__frequency = frequency
        self.__quantity = quantity

    def get_medication(self) -> Medication:
        return self.__medication

    def display_item(self):
        print(f"    - {self.__medication.get_name()}: {self.__dosage}, {self.__frequency}, Qty: {self.__quantity}")

class Prescription:
    def __init__(self, prx_id: str, date_prescribed: datetime, instructions: str,
                 doctor: Doctor, patient: Patient):
        self.__prescription_id = prx_id
        self.__date_prescribed = date_prescribed
        self.__instructions = instructions
        self.__doctor = doctor # Association: Doctor prescribes
        self.__patient = patient # Association: For Patient
        self.__items: List[PrescriptionItem] = [] # Association: Consists of multiple items

    def add_item(self, item: PrescriptionItem):
        self.__items.append(item)

    def display_prescription(self):
        print(f"  Prescription ID: {self.__prescription_id}")
        print(f"  Date: {self.__date_prescribed}, Doctor: {self.__doctor.get_username()}, Patient: {self.__patient.get_username()}")
        print(f"  Instructions: {self.__instructions}")
        print("  Items:")
        if self.__items:
            for item in self.__items:
                item.display_item()
        else:
            print("    No items in this prescription.")

class Pharmacy:
    def __init__(self, pharmacy_id: str, name: str, location: str):
        self.__pharmacy_id = pharmacy_id
        self.__name = name
        self.__location = location
        self.__stocked_medications: List[Medication] = [] # Association: Stocks multiple Medications

    def add_medication(self, medication: Medication):
        self.__stocked_medications.append(medication)
        print(f"'{medication.get_name()}' added to {self.__name} stock.")

    def get_medication_by_name(self, name: str) -> Optional[Medication]:
        for med in self.__stocked_medications:
            if med.get_name().lower() == name.lower():
                return med
        return None

    def display_stock(self):
        print(f"\n--- Stock in {self.__name} Pharmacy ---")
        if not self.__stocked_medications:
            print("No medications in stock.")
            return
        for med in self.__stocked_medications:
            med.display_medication_info()
        print("------------------------------------\n")

# --- 5. Billing Processing ---
class BillingItem:
    def __init__(self, item_id: str, description: str, quantity: int, unit_price: float):
        self.__item_id = item_id
        self.__description = description
        self.__quantity = quantity
        self.__unit_price = unit_price
        self.__subtotal = quantity * unit_price

    def get_subtotal(self) -> float:
        return self.__subtotal

    def display_item(self):
        print(f"  - {self.__description} (x{self.__quantity}) @ ${self.__unit_price:.2f} = ${self.__subtotal:.2f}")

class Invoice:
    def __init__(self, invoice_id: str, patient: Patient, date_issued: datetime):
        self.__invoice_id = invoice_id
        self.__patient = patient # Association: Patient receives Invoice
        self.__date_issued = date_issued
        self.__billing_items: List[BillingItem] = [] # Association: Includes multiple BillingItems
        self.__total_amount = 0.0
        self.__status = "Pending" # e.g., Pending, Paid
        self.__payments: List['Payment'] = [] # Association: Is settled by multiple Payments

    def add_billing_item(self, item: BillingItem):
        self.__billing_items.append(item)
        self.__total_amount += item.get_subtotal()

    def get_invoice_id(self) -> str:
        return self.__invoice_id

    def get_total_amount(self) -> float:
        return self.__total_amount

    def get_status(self) -> str:
        return self.__status

    def set_status(self, status: str):
        self.__status = status

    def add_payment(self, payment: 'Payment'):
        self.__payments.append(payment)
        # Logic to update invoice status based on payments could go here
        if sum(p.get_amount() for p in self.__payments) >= self.__total_amount:
            self.set_status("Paid")

    def get_payments(self) -> List['Payment']:
        return self.__payments

    def generate_invoice(self):
        print(f"\n--- Invoice {self.__invoice_id} for {self.__patient.get_username()} ---")
        print(f"Date Issued: {self.__date_issued.strftime('%Y-%m-%d %H:%M')}")
        print("Items:")
        for item in self.__billing_items:
            item.display_item()
        print(f"Total Amount: ${self.__total_amount:.2f}")
        print(f"Status: {self.__status}")
        print("Payments Made:")
        if self.__payments:
            for p in self.__payments:
                p.display_payment()
        else:
            print("  No payments made yet.")
        print("--------------------------------------------------\n")


class Payment:
    def __init__(self, payment_id: str, date: datetime, amount: float, method: str):
        self.__payment_id = payment_id
        self.__date = date
        self.__amount = amount
        self.__method = method
        self.__transaction_id = f"TRX{datetime.now().strftime('%Y%m%d%H%M%S')}" # Placeholder

    def get_amount(self) -> float:
        return self.__amount

    def display_payment(self):
        print(f"  Payment ID: {self.__payment_id}, Amount: ${self.__amount:.2f}, Method: {self.__method}, Date: {self.__date}")

# --- 6. Reviews & Feedback System ---
class HospitalService:
    def __init__(self, service_id: str, name: str, description: str, price: float):
        self.__service_id = service_id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__feedbacks: List[Feedback] = [] # Association: Service receives Feedbacks

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def add_feedback(self, feedback: 'Feedback'):
        self.__feedbacks.append(feedback)

    def display_service_info(self):
        print(f"Service: {self.__name} (ID: {self.__service_id}) - ${self.__price:.2f}")
        print(f"  Description: {self.__description}")

class Feedback:
    def __init__(self, feedback_id: str, rating: int, comment: str, date_submitted: datetime,
                 patient: Patient, service: HospitalService):
        self.__feedback_id = feedback_id
        self.__rating = rating # 1-5 stars
        self.__comment = comment
        self.__date_submitted = date_submitted
        self.__patient = patient # Association: Patient gives Feedback
        self.__service = service # Association: About HospitalService

    def display_feedback(self):
        print(f"Feedback ID: {self.__feedback_id}")
        print(f"Patient: {self.__patient.get_username()}, Service: {self.__service.get_name()}")
        print(f"Rating: {self.__rating} stars, Date: {self.__date_submitted}")
        print(f"Comment: \"{self.__comment}\"")


# --- Main Application Logic (Example Usage) ---
if __name__ == "__main__":
    # Create Users
    patient1 = Patient("P001", "AliceSmith", "pass123", "alice@example.com", date(1990, 5, 15), "Female")
    doctor1 = Doctor("D001", "Dr.Bob", "docpass", "bob@example.com", "Cardiology", "MD12345")
    pharmacist1 = Pharmacist("PH001", "Carol", "pharmpass", "carol@example.com", None) # Pharmacy will be assigned later

    # Create Hospital Services
    consultation_service = HospitalService("SVC001", "General Consultation", "Doctor's general check-up", 100.0)
    lab_test_service = HospitalService("SVC002", "Blood Test", "Routine blood work", 50.0)

    # Create a Pharmacy and Medications
    main_pharmacy = Pharmacy("PHRM001", "Central Hospital Pharmacy", "123 Pharmacy Lane")
    pharmacist1._Pharmacist__pharmacy = main_pharmacy # Assign pharmacy to pharmacist
    med1 = Medication("MED001", "Amoxicillin", "Antibiotic", 15.50, date(2026, 12, 31), 100)
    med2 = Medication("Paracetamol", "Pain Reliever", "Common pain relief", 5.00, date(2025, 6, 30), 200)
    main_pharmacy.add_medication(med1)
    main_pharmacy.add_medication(med2)
    main_pharmacy.display_stock()

    # Patient books an appointment
    appt1 = patient1.book_appointment(doctor1, datetime(2025, 7, 10, 10, 0), "Consultation")
    doctor1.approve_reject_appointment(appt1, "Confirmed")

    # Patient has a Medical Record
    patient_record = MedicalRecord("MR001", patient1)
    patient1.set_medical_record(patient_record)
    patient_record.add_diagnosis("Common Cold")
    patient_record.add_allergy("Penicillin")
    patient_record.add_treatment("Rest and fluids")
    patient1.view_medical_record()

    # Doctor prescribes medication
    amoxicillin_item = PrescriptionItem(med1, "500mg", "Twice daily", 10)
    paracetamol_item = PrescriptionItem(med2, "500mg", "As needed", 20)
    doctor1.prescribe_medication(patient1, [amoxicillin_item, paracetamol_item], "Take with food.")

    # View updated medical record with prescription
    patient1.view_medical_record()

    # Pharmacist manages stock
    pharmacist1.manage_stock_levels(med1, 90) # Sell 10 Amoxicillin
    main_pharmacy.display_stock()

    # Billing Process
    invoice1 = Invoice("INV001", patient1, datetime.now())
    patient1.add_invoice(invoice1) # Link invoice to patient

    invoice1.add_billing_item(BillingItem("BI001", "Doctor Consultation (Cardiology)", 1, consultation_service.get_price()))
    invoice1.add_billing_item(BillingItem("BI002", "Blood Test", 1, lab_test_service.get_price()))
    invoice1.add_billing_item(BillingItem("BI003", amoxicillin_item.get_medication().get_name(), amoxicillin_item.get_quantity(), amoxicillin_item.get_medication().get_price()))
    invoice1.add_billing_item(BillingItem("BI004", paracetamol_item.get_medication().get_name(), paracetamol_item.get_quantity(), paracetamol_item.get_medication().get_price()))

    invoice1.generate_invoice()

    # Patient makes payment
    patient1.make_payment(invoice1, 100.0, "UPI")
    invoice1.generate_invoice() # Check status

    patient1.make_payment(invoice1, invoice1.get_total_amount() - 100.0, "Credit Card")
    invoice1.generate_invoice() # Should now be "Paid"

    # Patient gives feedback
    patient1.give_feedback(consultation_service, 5, "Excellent consultation with Dr. Bob!")
    patient1.give_feedback(lab_test_service, 4, "Lab staff were efficient.")
    print("\n--- Feedback for Consultation Service ---")
    if consultation_service._HospitalService__feedbacks: # Accessing private attribute for demo
        for fb in consultation_service._HospitalService__feedbacks:
            fb.display_feedback()
