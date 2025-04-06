from django.db import models
from Clinicapp.models import LabDevice,StaffManage

# Create your models here.
        
class LabTest(models.Model):
    LaboratoryId = models.AutoField(primary_key=True)
    TestName = models.CharField(max_length=255)
    TestResult = models.TextField()
    ResultDate = models.DateTimeField(null=True, blank=True)
    DeviceCharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ServiceCharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    TestingCharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Technician = models.ForeignKey('Clinicapp.StaffManage', on_delete=models.SET_NULL, null=True, blank=True, related_name='conducted_tests')

    def __str__(self):
        return self.TestName
    
    @property
    def total_charges(self):
        return self.DeviceCharge + self.ServiceCharge + self.TestingCharge

class LabBill(models.Model):
    LabBillId = models.AutoField(primary_key=True)
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    LabTest = models.ForeignKey(LabTest, on_delete=models.SET_NULL, null=True, blank=True, related_name='lab_bills')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Automatic calculation of total price
        if self.LabTest:
            self.TotalPrice = self.LabTest.total_charges
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.LabBillId} for {self.LabTest.TestName if self.LabTest else 'Unknown Test'}"

    