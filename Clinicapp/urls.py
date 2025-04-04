from django.urls import path
from .views import (
    SignupAPIView,
    LoginApiView,
    DoctorCreateView,
    DoctorRetrieveUpdateApiView,
    StaffmanageCreateApiView,
    StaffmanageRetrieveApiView,
    PharmCreateApiView,
    PharmRetrieveUpdateApiView,
    LabdeviceCreateApiView,
    LabdeviceRetrieveUpdateView,
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    # Authentication 
    path('auth/signup/', SignupAPIView.as_view(), name='signup'),
    path('auth/login/', LoginApiView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Doctor 
    path('doctors/', DoctorCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateApiView.as_view(), name='doctor-retrieve-update'),
    
    # Staff management 
    path('staff/', StaffmanageCreateApiView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffmanageRetrieveApiView.as_view(), name='staff-retrieve-update'),
    
    # Pharmacy 
    path('pharmacy/', PharmCreateApiView.as_view(), name='pharmacy-list-create'),
    path('pharmacy/<int:pk>/', PharmRetrieveUpdateApiView.as_view(), name='pharmacy-retrieve-update'),
    
    # Lab device
    path('lab-devices/', LabdeviceCreateApiView.as_view(), name='lab-device-list-create'),
    path('lab-devices/<int:pk>/', LabdeviceRetrieveUpdateView.as_view(), name='lab-device-retrieve-update'),
]