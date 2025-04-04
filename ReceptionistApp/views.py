from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.utils.dateparse import parse_date
from .models import PatientDetails, Appointment, AppointmentBill
from .serializers import PatientSerializer, AppointmentSerializer, AppointmentBillSerializer

# Patient Management Views
class PatientListCreateView(generics.ListCreateAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class DeactivatePatientView(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, pk):
        try:
            patient = PatientDetails.objects.get(pk=pk)
            patient.is_active = False
            patient.save()
            return Response({"message": "Patient deactivated successfully"}, status=status.HTTP_200_OK)
        except PatientDetails.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

# Appointment Management Views
class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class CancelAppointmentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
            appointment.Status = 'cancelled'
            appointment.save()
            return Response({"message": "Appointment cancelled successfully"}, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)

# New View: List Appointments by Date
class AppointmentsByDateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        appointment_date = request.query_params.get('date')
        if not appointment_date:
            return Response({"error": "Date parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            parsed_date = parse_date(appointment_date)
            appointments = Appointment.objects.filter(date=parsed_date)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

# Appointment Listing Views
class AppointmentsByPatientView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patientId']
        return Appointment.objects.filter(patient_id=patient_id)

class AppointmentsByDoctorView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        doctor_id = self.kwargs['doctorId']
        return Appointment.objects.filter(doctor_id=doctor_id)

class AppointmentsByStatusView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status_param = self.request.query_params.get('status')
        return Appointment.objects.filter(status=status_param)

# Appointment Billing Views
class AppointmentBillListCreateView(generics.ListCreateAPIView):
    queryset = AppointmentBill.objects.all()
    serializer_class = AppointmentBillSerializer
    permission_classes = [IsAuthenticated]

class AppointmentBillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppointmentBill.objects.all()
    serializer_class = AppointmentBillSerializer
    permission_classes = [IsAuthenticated]

# New View: List Bills by Date Range
class BillsByDateRangeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')

        if not start_date or not end_date:
            return Response({"error": "Start date and end date are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            parsed_start_date = parse_date(start_date)
            parsed_end_date = parse_date(end_date)
            
            if not parsed_start_date or not parsed_end_date:
                return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

            bills = AppointmentBill.objects.filter(date__range=(parsed_start_date, parsed_end_date))
            serializer = AppointmentBillSerializer(bills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)
