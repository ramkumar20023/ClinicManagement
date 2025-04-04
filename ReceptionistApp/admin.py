from django.contrib import admin
from .models import PatientDetails, Appointment, AppointmentBill

@admin.register(PatientDetails)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('PatientId', 'FirstName', 'LastName', 'Gender', 'PhoneNumber', 'is_active')
    search_fields = ('FirstName', 'LastName', 'PhoneNumber')
    list_filter = ('Gender', 'BloodGroup', 'is_active')
    ordering = ('-RegistrationDate',)  # New: Sort by most recent patients
    list_editable = ('is_active',)  # New: Allow quick activation/deactivation

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('AppointmentId', 'get_patient_name', 'get_doctor_name', 'AppointmentDate', 'Status')
    list_filter = ('Status', 'Doctor', 'AppointmentDate')
    search_fields = ('Patient__FirstName', 'Patient__LastName', 'Doctor__FirstName', 'Doctor__LastName')
    ordering = ('-AppointmentDate',)  # New: Show upcoming appointments first

    def get_patient_name(self, obj):
        return obj.Patient.full_name
    get_patient_name.short_description = 'Patient'

    # def get_doctor_name(self, obj):
    #     return obj.Doctor.full_name()
    # get_doctor_name.short_description = 'Doctor'

    def get_doctor_name(self, obj):
        return obj.Doctor.full_name if obj.Doctor else "No Doctor"
    get_doctor_name.admin_order_field = 'Doctor'  # Allows sorting by Doctor
    get_doctor_name.short_description = 'Doctor Name'  # Label for the admin panel


@admin.register(AppointmentBill)
class AppointmentBillAdmin(admin.ModelAdmin):
    list_display = ('BillId', 'get_appointment', 'TotalCost', 'CreatedAt')
    search_fields = ('Appointment__Patient__FirstName', 'Appointment__Patient__LastName')
    ordering = ('-CreatedAt',)  # New: Show latest bills first

    def get_appointment(self, obj):
        return f"Appointment #{obj.Appointment.AppointmentId}"
    get_appointment.short_description = 'Appointment'
