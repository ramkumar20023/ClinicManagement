from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PatientDetails, Appointment, AppointmentBill

@admin.register(PatientDetails)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('PatientId', 'FirstName', 'LastName', 'Gender', 'phonenumber')
    search_fields = ('FirstName', 'LastName', 'phonenumber')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('AppointmentId', 'get_patient_name', 'get_doctor_name', 'AppointmentDate', 'Status')
    list_filter = ('Status', 'Doctor')
    
    def get_patient_name(self, obj):
        return obj.PatientDetails.full_name
    get_patient_name.short_description = 'Patient'
    
    def get_doctor_name(self, obj):
        return obj.Doctor.full_name()
    get_doctor_name.short_description = 'Doctor'

@admin.register(AppointmentBill)
class AppointmentBillAdmin(admin.ModelAdmin):
    list_display = ('BillId', 'get_appointment', 'Total_cost')
    
    def get_appointment(self, obj):
        return f"Appointment #{obj.Appointment.AppointmentId}"
    get_appointment.short_description = 'Appointment'