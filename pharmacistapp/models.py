from django.db import models
from decimal import Decimal
from Clinicapp.models import Pharm

# Create your models here.

# Pharmacist Models
class Pharmacist(models.Model):
    PharmId = models.AutoField(primary_key=True)
    Pharm = models.ForeignKey('Clinicapp.Pharm', on_delete=models.SET_NULL, null=True, blank=True, related_name='pharmacy_pharmacists')
    Appointment = models.ForeignKey('ReceptionistApp.Appointment', on_delete=models.CASCADE, null=True, blank=True, related_name='pharmacy_orders')
    Quantity = models.IntegerField(default=1)  

    @property
    def MedicineName(self):
        """Get medicine name from linked Pharm record"""
        return self.Pharm.MedicineName if self.Pharm else ""

    @property
    def PricePerUnit(self):
        """Get price from linked Pharm record"""
        return self.Pharm.PricePerUnit if self.Pharm else 0.00

    @property
    def total_price(self):
        """Calculate total price based on quantity and Pharm's price"""
        return self.Quantity * self.PricePerUnit

    def __str__(self):
        return f"{self.MedicineName} x{self.Quantity} (Appt: {self.Appointment.AppointmentId if self.Appointment else 'None'})"
  
class PharmBill(models.Model):
    BillId = models.AutoField(primary_key=True)
    Pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    GST = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('18.00')) 
    FinalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Created_at = models.DateTimeField(auto_now_add=True)
    Appointment = models.ForeignKey('ReceptionistApp.Appointment', on_delete=models.CASCADE, null=True, blank=True, related_name='pharmacy_bills')

    def save(self, *args, **kwargs):
        if self.Pharmacist and self.Pharmacist.total_price is not None:
            self.TotalPrice = Decimal(self.Pharmacist.total_price)
            gst_decimal = Decimal(self.GST)
            self.FinalPrice = self.TotalPrice + (self.TotalPrice * gst_decimal / Decimal(100))
        else:
            self.TotalPrice = Decimal(0.00)
            self.FinalPrice = Decimal(0.00)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.BillId} - Final Price: {self.FinalPrice}"