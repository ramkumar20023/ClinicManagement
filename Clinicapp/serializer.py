from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Userdetails,User
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,Group
from .models import Role,Department,Doctor,StaffManage,Pharm,Batch,LabDevice

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'

class userdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userdetails
        fields='__all__'
        # fields=['id','name']

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        fields=('id','username')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")
        return data

class Signupserializer(serializers.ModelSerializer):
    group_name = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'group_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        group_name = validated_data.pop('group_name')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        return user

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

    def validate_contact(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Contact must be a 10-digit number.")
        return value

class StaffmanageSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffManage
        fields='__all__'
    
    def validate_contact(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Contact must be a 10-digit number.")
        return value

class PharmSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pharm
        fields='__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Batch
        fields='__all__'

class LabDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabDevice
        fields='__all__'

