from rest_framework import serializers
from .models import Pharmacist, PharmBill

class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = '__all__'

class PharmBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmBill
        fields = '__all__'