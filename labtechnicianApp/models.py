from django.db import models
from ReceptionistApp.models import PatientDetails

class LabTest(models.Model):
    LaboratoryId = models.AutoField(primary_key=True)
    TestName = models.CharField(max_length=255)
    TestResult = models.TextField()
    ResultDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sample_No = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    patientinform = models.ForeignKey(PatientDetails, on_delete=models.SET_NULL, null=True, blank=True, related_name='patient_information')
    Reffered_by = models.ForeignKey('Doctorapp.doctorinform', on_delete=models.CASCADE, null=True, blank=True)
    consultant = models.ForeignKey('Doctorapp.Consultation', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.TestName

class LabBill(models.Model):
    LabBillId = models.AutoField(primary_key=True)
    DeviceCharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ServiceCharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    TestingCharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    LabTest = models.ForeignKey(LabTest, on_delete=models.SET_NULL, null=True, blank=True, related_name='lab_bills')
    patientinform = models.ForeignKey('ReceptionistApp.PatientDetails', on_delete=models.SET_NULL, null=True, blank=True)
    Reffered = models.ForeignKey('Doctorapp.doctorinform', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.TotalPrice = (self.DeviceCharge or 0) + (self.ServiceCharge or 0) + (self.TestingCharge or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.LabBillId} for {self.LabTest.TestName if self.LabTest else 'Unknown Test'}"