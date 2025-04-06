from rest_framework import serializers
from .models import LabTest, LabBill
from Clinicapp.models import LabDevice

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = '__all__'

class LabBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabBill
        fields = '__all__'

class LabDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabDevice
        fields = ['ModuleId', 'EquipmentName', 'Status']
        read_only_fields = ['ModuleId', 'EquipmentName']