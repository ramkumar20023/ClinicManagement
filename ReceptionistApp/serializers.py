from rest_framework import serializers
from .models import PatientDetails, Appointment, AppointmentBill

class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = PatientDetails
        fields = '__all__'

    def validate_PhoneNumber(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Enter a valid phone number with at least 10 digits.")
        return value

class AppointmentSerializer(serializers.ModelSerializer):
    get_patient_name = serializers.ReadOnlyField(source="PatientDetails.full_name")
    get_doctor_name = serializers.ReadOnlyField(source="Doctor.full_name")

    class Meta:
        model = Appointment
        fields = '__all__'

    def validate_AppointmentDate(self, value):
        from django.utils.timezone import now
        if value < now():
            raise serializers.ValidationError("Appointment date must be in the future.")
        return value

class AppointmentBillSerializer(serializers.ModelSerializer):
    get_appointment_details = serializers.ReadOnlyField(source="Appointment.__str__")

    class Meta:
        model = AppointmentBill
        fields = '__all__'

    def validate_Consultant_fees(self, value):
        if value < 0:
            raise serializers.ValidationError("Consultation fees cannot be negative.")
        return value

    def validate_ServiceCharge(self, value):
        if value < 0:
            raise serializers.ValidationError("Service charge cannot be negative.")
        return value
