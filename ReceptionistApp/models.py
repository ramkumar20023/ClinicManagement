from django.db import models
from Clinicapp.models import Doctor

# Create your models here.

# Receptionist Models

from django.utils.timezone import now

class PatientDetails(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'other', 'Other'

    class BloodChoices(models.TextChoices):
        A_POSITIVE = 'A+', 'A+'
        A_NEGATIVE = 'A-', 'A-'
        B_POSITIVE = 'B+', 'B+'
        B_NEGATIVE = 'B-', 'B-'
        AB_POSITIVE = 'AB+', 'AB+'
        AB_NEGATIVE = 'AB-', 'AB-'
        O_POSITIVE = 'O+', 'O+'
        O_NEGATIVE = 'O-', 'O-'

    PatientId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Age = models.IntegerField()
    DOB = models.DateField()
    Gender = models.CharField(max_length=20, choices=GenderChoices.choices)
    BloodGroup = models.CharField(max_length=20, choices=BloodChoices.choices, default=BloodChoices.O_POSITIVE)
    Address = models.TextField()
    PhoneNumber = models.CharField(max_length=15)
    EmergencyContact = models.CharField(max_length=15)
    Allergy = models.TextField(blank=True, null=True)
    RegistrationDate = models.DateTimeField(auto_now_add=True)
    LastVisitDate = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

    @property
    def full_name(self):
        return f"{self.FirstName} {self.LastName}"


class Appointment(models.Model):
    class StatusChoices(models.TextChoices):
        SCHEDULED = 'scheduled', 'Scheduled'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    AppointmentId = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE, related_name='patient_appointments')
    Doctor = models.ForeignKey('Clinicapp.Doctor', on_delete=models.CASCADE, related_name='doctor_appointments')
    AppointmentDate = models.DateTimeField()
    Status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.SCHEDULED)
    Remarks = models.TextField(blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        patient_name = self.Patient.full_name if self.Patient else "No Patient"
        doctor_name = self.Doctor.full_name if self.Doctor else "No Doctor"
        return f"Appointment #{self.AppointmentId} - {patient_name} with {doctor_name}"


class AppointmentBill(models.Model):
    BillId = models.AutoField(primary_key=True)
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointment_bills')
    ConsultantFees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ServiceCharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    TotalCost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatic calculation of total cost
        self.TotalCost = self.ConsultantFees + self.ServiceCharge
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.BillId} for Appointment #{self.Appointment.AppointmentId}"