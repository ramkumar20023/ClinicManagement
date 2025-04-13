from rest_framework import serializers
from .models import doctorinform,Prescription,Consultation,LabTestReport,PatientHistory
from django.contrib.auth.models import User

class DoctorinformSerializer(serializers.ModelSerializer):
    class Meta:
        model=doctorinform
        fields='__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields='__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consultation
        fields='__all__'

class LabTestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabTestReport
        fields='__all__'

class PatienthistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientHistory
        fields='__all__'