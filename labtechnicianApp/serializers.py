from rest_framework import serializers
from .models import LabTest, LabBill, User
from Clinicapp.models import LabDevice
from django.contrib.auth.models import User, Group 
from django.contrib.auth.hashers import make_password
from .models import AvailableLabTest

class LabTestSerializer(serializers.ModelSerializer):
    date_only =serializers.SerializerMethodField()
    time_only =serializers.SerializerMethodField()
    def get_date_only(self, obj):
        return obj. created_at.date().strftime('%Y-%m-%d') if obj. created_at else None
    
    def get_time_only(self, obj):
        return obj. created_at.time().strftime('%H:%M:%S') if obj. created_at else None
    class Meta:
        model = LabTest
        fields = '__all__'
        fields = ['LaboratoryId', 'TestName', 'TestResult', 'ResultDate', 'sample_No', 'created_at', 'patientinform', 'Reffered_by', 'consultant','date_only','time_only']

class LabBillSerializer(serializers.ModelSerializer):
    date_only = serializers.SerializerMethodField()
    time_only = serializers.SerializerMethodField()

    def get_date_only(self, obj):
        return obj.created_at.date().strftime('%Y-%m-%d') if obj.created_at else None

    def get_time_only(self, obj):
        return obj.created_at.time().strftime('%H:%M:%S') if obj.created_at else None

    class Meta:
        model = LabBill
        fields = [
            'LabBillId', 'DeviceCharge', 'ServiceCharge', 'TestingCharge',
            'TotalPrice', 'LabTest', 'patientinform', 'Reffered',
            'created_at', 'date_only', 'time_only'
        ]

class LabDeviceSerializer(serializers.ModelSerializer):
    date_only = serializers.SerializerMethodField()
    hour_only = serializers.SerializerMethodField()

    def get_date_only(self, obj):
        return obj.Date.strftime('%Y-%m-%d') if obj.Date else None

    def get_hour_only(self, obj):
        return obj.Date.strftime('%H:%M:%S') if obj.Date else None  # e.g., 01 PM

    class Meta:
        model = LabDevice
        fields = [
            'ModuleId',
            'EquipmentName',
            'Quantity',
            'Date',
            'Last_Service_Date',
            'Next_Service_Date',
            'Status',
            'date_only',
            'hour_only'
        ]



class SignupSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(write_only=True,required=False)

    def create(self,validated_data):
        group_name = validated_data.pop('group_name',None)
        
        validated_data["password"] = make_password(validated_data.get("password"))

        user=super(SignupSerializer,self).create(validated_data)
        if group_name:
            group,created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
        return user
    class Meta:
        model = User 
        fields = ['username','password','group_name']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username','password']
    password = serializers.CharField()






class AvailableLabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableLabTest
        fields = '__all__'