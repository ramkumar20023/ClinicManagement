from django.shortcuts import render
from .models import doctorinform,Prescription,Consultation,LabTestReport,PatientHistory
from .serializer import (DoctorinformSerializer,PrescriptionSerializer,ConsultationSerializer,
                         LabTestReportSerializer,PatienthistorySerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from django.shortcuts import get_object_or_404
from Clinicapp.permissions import IsDoctor

# Create your views here.
class DoctorinformCreateApiview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request):
        doctors=doctorinform.objects.all()
        serializer=DoctorinformSerializer(doctors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=DoctorinformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DoctorinformReteriveupdateApiview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request, pk):
        Doctors=get_object_or_404(doctorinform, pk=pk)
        serializer=DoctorinformSerializer(Doctors)
        return Response(serializer.data)
    
    def put(self, request, pk):
        doctors=get_object_or_404(doctorinform, pk=pk)
        serializer=DoctorinformSerializer(doctors, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        doctors=get_object_or_404(doctorinform, pk=pk)
        doctors.delete()
        return Response({"Message":"Doctor information Deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class PrescriptioncreateApiview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request):
        Prescriptions=Prescription.objects.all()
        serializer=PrescriptionSerializer(Prescriptions, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serilaizer=PrescriptionSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PrescriptionRetrieveupdateApiview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request, pk):
        Prescriptions=get_object_or_404(Prescription, pk=pk)
        serilaizer=PrescriptionSerializer(Prescriptions, data=request.data)
        return Response(serilaizer.data)
    
    def put(self, request, pk):
        Prescriptions=get_object_or_404(Prescription, pk=pk)
        serializer=PrescriptionSerializer(Prescriptions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        Prescriptions=get_object_or_404(Prescription, pk=pk)
        Prescriptions.delete()
        return Response({"Message":"Prescription Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class ConsulationcreateApiview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request):
        Consultant=Consultation.objects.all()
        serializer=ConsultationSerializer(Consultant, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ConsulatntRetrieveupdateApiview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request, pk):
        consultant=get_object_or_404(Consultation, pk=pk)
        serilaizer=ConsultationSerializer(consultant)
        return Response(serilaizer.data)
    
    def put(self, request, pk):
        consultant=get_object_or_404(Consultation, pk=pk)
        serializer=ConsultationSerializer(consultant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        consultant=get_object_or_404(Consultation, pk=pk)
        consultant.delete()
        return Response({"Message":"Consultation Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        
class LabtestReportCreateApiview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request):
        Testreport=LabTestReport.objects.all()
        serializer=LabTestReportSerializer(Testreport, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=LabTestReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LabtestRetrieveupdateApiview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request, pk):
        Testreport=get_object_or_404(LabTestReport, pk=pk)
        serializer=LabTestReportSerializer(Testreport)
        return Response(serializer.data)
    
    def put(self, request, pk):
        Testreport=get_object_or_404(LabTestReport, pk=pk)
        serializer=LabTestReportSerializer(Testreport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        Testreport=get_object_or_404(LabTestReport, pk=pk)
        Testreport.delete()
        return Response({"Message":"Lab Report Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class PatienthistorycreateApiview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request):
        patienthistorys=PatientHistory.objects.all()
        serializer=PatienthistorySerializer(patienthistorys, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=PatienthistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatienthistoryRetrieveupdateview(APIView):
    permission_classes=[permissions.IsAuthenticated, IsDoctor]
    def get(self, request, pk):
        patienthistory=get_object_or_404(PatientHistory, pk=pk)
        serializer=PatienthistorySerializer(patienthistory)
        return Response(serializer.data)
    
    def put(self, request, pk):
        patienthistory=get_object_or_404(PatientHistory, pk=pk)
        serializer=PatienthistorySerializer(patienthistory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        patienthistory=get_object_or_404(PatientHistory, pk=pk)
        patienthistory.delete()
        return Response({"Message":"patient History Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)