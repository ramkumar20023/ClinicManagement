from django.db import models
from ReceptionistApp.models import Appointment
from Clinicapp.models import Pharm, Department

class doctorinform(models.Model):
    informId = models.AutoField(primary_key=True)
    DoctorName = models.CharField(max_length=100)
    specialist = models.ForeignKey('Clinicapp.Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='DOctor_specialist')

    def __str__(self):
        return self.DoctorName

class Prescription(models.Model):
    PrescriptionId = models.AutoField(primary_key=True)
    Frequency = models.CharField(max_length=100)
    Dosage = models.CharField(max_length=100)
    No_of_Days = models.IntegerField()
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescriptions')
    Medicine = models.ForeignKey(Pharm, on_delete=models.SET_NULL, null=True, blank=True, related_name='prescribed_medicines')
    Created_at = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return f"Prescription #{self.Frequency}"

class Consultation(models.Model):
    ConsultantId = models.AutoField(primary_key=True)
    Notes = models.TextField()
    Prescription = models.ForeignKey(Prescription, on_delete=models.SET_NULL, null=True, blank=True, related_name='consultations')
    LabTesting = models.ForeignKey('labtechnicianApp.LabTest', on_delete=models.SET_NULL, blank=True, null=True, related_name='consultations')
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='consultations')
    doctordetail = models.ForeignKey(doctorinform, on_delete=models.SET_NULL, blank=True, null=True)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation #{self.ConsultantId}"

class LabTestReport(models.Model):
    ReportID = models.AutoField(primary_key=True)
    LabTesting = models.ForeignKey('labtechnicianApp.LabTest', on_delete=models.CASCADE, related_name='reports')
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='lab_reports')
    Findings = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Report #{self.ReportID} for {self.LabTesting.TestName}"

class PatientHistory(models.Model):
    RecordId = models.AutoField(primary_key=True)
    Consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='history_records')
    report = models.ForeignKey(LabTestReport, on_delete=models.CASCADE, null=True, blank=True)
    Diagnosis = models.TextField()
    Treatment = models.TextField()
    doctorname = models.ForeignKey(doctorinform, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"History Record #{self.RecordId}"