from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Pharmacist, PharmBill
from .serializers import PharmacistSerializer, PharmBillSerializer

class PharmacistAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                pharmacist = Pharmacist.objects.get(pk=pk)
                serializer = PharmacistSerializer(pharmacist)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Pharmacist.DoesNotExist:
                return Response({"error": "Pharmacist not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            pharmacists = Pharmacist.objects.all()
            serializer = PharmacistSerializer(pharmacists, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     serializer = PharmacistSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            pharmacist = Pharmacist.objects.get(pk=pk)
            serializer = PharmacistSerializer(pharmacist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pharmacist.DoesNotExist:
            return Response({"error": "Pharmacist not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            pharmacist = Pharmacist.objects.get(pk=pk)
            pharmacist.delete()
            return Response({"message": "Pharmacist deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Pharmacist.DoesNotExist:
            return Response({"error": "Pharmacist not found"}, status=status.HTTP_404_NOT_FOUND)


class PharmBillAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                pharm_bill = PharmBill.objects.get(pk=pk)
                serializer = PharmBillSerializer(pharm_bill)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PharmBill.DoesNotExist:
                return Response({"error": "PharmBill not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            pharm_bills = PharmBill.objects.all()
            serializer = PharmBillSerializer(pharm_bills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PharmBillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "PharmBill generated successfully",
                "bill_details": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            pharm_bill = PharmBill.objects.get(pk=pk)
            serializer = PharmBillSerializer(pharm_bill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PharmBill.DoesNotExist:
            return Response({"error": "PharmBill not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            pharm_bill = PharmBill.objects.get(pk=pk)
            pharm_bill.delete()
            return Response({"message": "PharmBill deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except PharmBill.DoesNotExist:
            return Response({"error": "PharmBill not found"}, status=status.HTTP_404_NOT_FOUND)