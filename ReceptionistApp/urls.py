from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PatientListCreateView, PatientDetailView, DeactivatePatientView,
    AppointmentListCreateView, AppointmentDetailView, CancelAppointmentView,
    AppointmentBillListCreateView, AppointmentBillDetailView,
    AppointmentsByPatientView, AppointmentsByDoctorView, AppointmentsByStatusView,
    AppointmentsByDateView, BillsByDateRangeView
)

urlpatterns = [
    # JWT Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Patient Endpoints
    path('patients/', PatientListCreateView.as_view(), name='list-create-patients'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='get-update-patient'),
    path('patients/<int:pk>/deactivate/', DeactivatePatientView.as_view(), name='deactivate-patient'),

    # Appointment Endpoints
    path('appointments/', AppointmentListCreateView.as_view(), name='create-appointment'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='get-update-appointment'),
    path('appointments/<int:pk>/cancel/', CancelAppointmentView.as_view(), name='cancel-appointment'),
    path('appointments/by-date/', AppointmentsByDateView.as_view(), name='appointments-by-date'),

    # Appointment Filtering
    path('appointments/patient/<int:patientId>/', AppointmentsByPatientView.as_view(), name='appointments-by-patient'),
    path('appointments/doctor/<int:doctorId>/', AppointmentsByDoctorView.as_view(), name='appointments-by-doctor'),
    path('appointments/status/', AppointmentsByStatusView.as_view(), name='appointments-by-status'),

    # Billing Endpoints
    path('bills/', AppointmentBillListCreateView.as_view(), name='list-create-bills'),
    path('bills/<int:pk>/', AppointmentBillDetailView.as_view(), name='get-update-bill'),
    path('bills/by-date-range/', BillsByDateRangeView.as_view(), name='bills-by-date-range'),
]
