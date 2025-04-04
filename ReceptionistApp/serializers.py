from rest_framework import serializers
from .models import PatientDetails, Appointment, AppointmentBill

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate_date(self, value):
        if value is None:
            raise serializers.ValidationError("Appointment date cannot be empty.")
        return value

class AppointmentBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentBill
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Bill amount must be greater than zero.")
        return value
