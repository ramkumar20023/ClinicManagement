from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import viewsets
from rest_framework import status,permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
from .models import Doctor,StaffManage,Pharm,LabDevice

from .serializer import (RoleSerializer,Signupserializer,LoginSerializer,DepartmentSerializer,
                         DoctorSerializer,StaffmanageSerializer,PharmSerializer,BatchSerializer,
                         LabDeviceSerializer,userdetailsSerializer,Userserializer)
from django.shortcuts import get_object_or_404
from .models import User,Userdetails
from .permissions import IsAdmin

class SignupAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = Signupserializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            
            # Get user details if they exist
            user_details = {}
            if hasattr(user, 'userdetails'):
                user_details = userdetailsSerializer(user.userdetails).data
            
            # Get the role/group name
            role = None
            if user.groups.exists():
                role = user.groups.first().name
            
            return Response({
                "status": status.HTTP_201_CREATED,
                "message": "User registered and logged in successfully",
                "user_id": user.id,
                "username": user.username,
                "role": role,
                "user_details": user_details,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Registration failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Bad Request",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        
        # Get the role/group name
        role = None
        if user.groups.exists():
            role = user.groups.first().name
            
        return Response({
            "status": status.HTTP_200_OK,
            "message": "Login success",
            "user_id": user.id,
            "username": user.username,
            "role": role,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_200_OK)
        
class userDetailsViewSet(viewsets.ModelViewSet):
    queryset=Userdetails.objects.all()
    serializer_class=userdetailsSerializer
    permission_classes=[]
    # permission_classes=[IsAuthenticated] # can access only logged in user

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=Userserializer
    permission_classes=[]
    

class DoctorCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated | IsAdmin]

    def get(self, request):
        Doctors=Doctor.objects.all()
        serializer=DoctorSerializer(Doctors, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DoctorRetrieveUpdateApiView(APIView):
    permission_classes=[permissions.IsAuthenticated | IsAdmin]

    def get(self, request, pk):
        Doctors=get_object_or_404(Doctor, pk=pk)
        serializer=DoctorSerializer(Doctors)
        return Response(serializer.data)
    
    def put(self, request, pk):
        Doctors=get_object_or_404(Doctor, pk=pk)
        serializer=DoctorSerializer(Doctors, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        Doctors=get_object_or_404(Doctor, pk=pk)
        Doctors.delete()
        return Response({"message": "Doctor Details deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class StaffmanageCreateApiView(APIView):
    permission_classes=[permissions.IsAuthenticated | IsAdmin]

    def get(self, request):
        Staff=StaffManage.objects.all()
        serializer=StaffmanageSerializer(Staff, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StaffmanageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StaffmanageRetrieveApiView(APIView):
    permission_classes=[permissions.IsAuthenticated | IsAdmin]

    def get(self, request, pk):
        staff=get_object_or_404(StaffManage, pk=pk)
        serializer=StaffmanageSerializer(staff)
        return Response(serializer.data)
    
    def put(self, request, pk):
        staff=get_object_or_404(Doctor, pk=pk)
        serializer=StaffmanageSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        staff=get_object_or_404(StaffManage, pk=pk)
        staff.delete()
        return Response({"message": "Staff Details deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class PharmCreateApiView(APIView):
    permission_classes=[permissions.IsAuthenticated | IsAdmin]

    def get(self, request):
        medical=Pharm.objects.all()
        serializer=PharmSerializer(medical, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=PharmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PharmRetrieveUpdateApiView(APIView):
    permission_classes=[permissions.IsAuthenticated | IsAdmin]

    def get(self, request, pk):
        medical=get_object_or_404(Pharm, pk=pk)
        serializer=PharmSerializer(medical)
        return Response(serializer.data)
    
    def put(self, request, pk):
        medical=get_object_or_404(Pharm, pk=pk)
        serializer=PharmSerializer(medical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        medical=get_object_or_404(Pharm, pk=pk)
        medical.delete()
        return Response({"message": "Medicines Details deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class LabdeviceCreateApiView(APIView):
    permission_classes=[permissions.IsAuthenticated | IsAdmin]

    def get(self, request):
        lab=LabDevice.objects.all()
        serializer=LabDeviceSerializer(lab, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=LabDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LabdeviceRetrieveUpdateView(APIView):
    permission_classes=[permissions.IsAuthenticated | IsAdmin]

    def get(self, request, pk):
        labtech=get_object_or_404(LabDevice, pk=pk)
        serializer=LabDeviceSerializer(labtech)
        return Response(serializer.data)
    
    def put(self, request, pk):
        labtech=get_object_or_404(LabDevice, pk=pk)
        serializer=LabDeviceSerializer(labtech, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        labtech=get_object_or_404(LabDevice, pk=pk)
        labtech.delete()
        return Response({"message": "LabEquipment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)