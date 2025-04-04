from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import LabTest, LabBill, LabDevice
from django.shortcuts import get_object_or_404
from .serializers import LabTestSerializer, LabBillSerializer,LabDeviceSerializer

# LabTest API View
class LabTestAPIView(APIView):
    permissions_classes=[IsAuthenticated]
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
    permissions_classes=[IsAuthenticated]
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
    permission_classes=[IsAuthenticated]

    def get(self, request):
        lab=LabDevice.objects.all()
        serializer=LabDeviceSerializer(lab, many=True)
        return Response(serializer.data)
class LabdeviceRetrieveUpdateView(APIView):
    permission_classes=[IsAuthenticated]

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