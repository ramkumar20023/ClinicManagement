from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.permissions import IsAuthenticated
from .models import LabTest, LabBill 
from django.contrib.auth.models import User
from Clinicapp.models import LabDevice
from django.shortcuts import get_object_or_404
from .serializers import LabTestSerializer, LabBillSerializer,LabDeviceSerializer
from Clinicapp.permissions import IsLabTechnician
from .serializers import SignupSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import AvailableLabTest
from .serializers import AvailableLabTestSerializer
from rest_framework import generics



# LabTest API View
class LabtechnicianDashboard(APIView):
    permission_classes = [permissions.IsAuthenticated, IsLabTechnician]
    
    def get(self, request):
        return Response({
            "message": "Welcome LabTechnician",
            "data": "Lab Technician dashboard data"
        })


class LabTestAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsLabTechnician]

    def get(self, request, pk=None):
        if pk:
            try:
                lab_test = LabTest.objects.get(pk=pk)
                serializer = LabTestSerializer(lab_test)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except LabTest.DoesNotExist:
                return Response({"error": "LabTest not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            lab_tests = LabTest.objects.all()
            serializer = LabTestSerializer(lab_tests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LabTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            lab_test = LabTest.objects.get(pk=pk)
            serializer = LabTestSerializer(lab_test, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except LabTest.DoesNotExist:
            return Response({"error": "LabTest not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            lab_test = LabTest.objects.get(pk=pk)
            lab_test.delete()
            return Response({"message": "LabTest deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except LabTest.DoesNotExist:
            return Response({"error": "LabTest not found"}, status=status.HTTP_404_NOT_FOUND)


# LabBill API View
class LabBillAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsLabTechnician]

    def get(self, request, pk=None):
        if pk:
            try:
                lab_bill = LabBill.objects.get(pk=pk)
                serializer = LabBillSerializer(lab_bill)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except LabBill.DoesNotExist:
                return Response({"error": "LabBill not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            lab_bills = LabBill.objects.all()
            serializer = LabBillSerializer(lab_bills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LabBillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            lab_bill = LabBill.objects.get(pk=pk)
            serializer = LabBillSerializer(lab_bill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except LabBill.DoesNotExist:
            return Response({"error": "LabBill not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            lab_bill = LabBill.objects.get(pk=pk)
            lab_bill.delete()
            return Response({"message": "LabBill deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except LabBill.DoesNotExist:
            return Response({"error": "LabBill not found"}, status=status.HTTP_404_NOT_FOUND)


class LabdeviceCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsLabTechnician]


    def get(self, request):
        lab=LabDevice.objects.all()
        serializer=LabDeviceSerializer(lab, many=True)
        return Response(serializer.data)
    
class LabdeviceRetrieveUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsLabTechnician]

    lookup_field = 'ModuleId'

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



class AvailableLabTestListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsLabTechnician]

    def get(self, request):
        lab_tests = AvailableLabTest.objects.all()
        serializer = AvailableLabTestSerializer(lab_tests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvailableLabTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AvailableLabTestRetrieveUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsLabTechnician]

    def get(self, request, pk):
        lab_test = get_object_or_404(AvailableLabTest, pk=pk)
        serializer = AvailableLabTestSerializer(lab_test)
        return Response(serializer.data)

    def put(self, request, pk):
        lab_test = get_object_or_404(AvailableLabTest, pk=pk)
        serializer = AvailableLabTestSerializer(lab_test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        lab_test = get_object_or_404(AvailableLabTest, pk=pk)
        lab_test.delete()
        return Response({"message": "Lab test deleted successfully"}, status=status.HTTP_204_NO_CONTENT)






class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "status": status.HTTP_200_OK,
                    "message": "Login successful",
                    "username": user.username,
                    "role": user.groups.first().id if user.groups.exists() else "No role assigned",
                    "tokens": {
                        "access": str(refresh.access_token),
                        "refresh": str(refresh)
                    }
                }, status=status.HTTP_200_OK)

            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Invalid username or password"
            }, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Invalid data",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from Clinicapp.models import LabDevice
from Clinicapp.permissions import IsLabTechnician
from rest_framework.permissions import IsAuthenticated

@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsLabTechnician])
def update_labdevice_status(request, pk):
    try:
        lab_device = LabDevice.objects.get(pk=pk)
    except LabDevice.DoesNotExist:
        return Response({"error": "LabDevice not found"}, status=status.HTTP_404_NOT_FOUND)

    new_status = request.data.get("Status")
    if new_status:
        lab_device.Status = new_status
        lab_device.save()
        return Response({"message": "Status updated successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "No status provided"}, status=status.HTTP_400_BAD_REQUEST)







