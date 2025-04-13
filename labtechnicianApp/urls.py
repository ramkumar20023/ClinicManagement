from django.urls import path
from .views import LabTestAPIView, LabBillAPIView,LabdeviceCreateApiView, LabdeviceRetrieveUpdateView,LabtechnicianDashboard

urlpatterns = [
    path('labtests/', LabTestAPIView.as_view(), name='labtest-list'),
    path('labtests/<int:pk>/', LabTestAPIView.as_view(), name='labtest-detail'),
    path('labbills/', LabBillAPIView.as_view(), name='labbill-list'),
    path('labbills/<int:pk>/', LabBillAPIView.as_view(), name='labbill-detail'),
    path('devices/', LabdeviceCreateApiView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', LabdeviceRetrieveUpdateView.as_view(), name='device-retrieve-update'),
    path('labdashboard/', LabtechnicianDashboard.as_view(), name='labtechnician-dashboard'),
]