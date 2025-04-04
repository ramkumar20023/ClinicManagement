from django.urls import path
from .views import LabTestAPIView, LabBillAPIView,LabdeviceCreateApiView, LabdeviceRetrieveUpdateView

urlpatterns = [
    path('labtests/', LabTestAPIView.as_view(), name='labtest-list'),
    path('labtests/<int:pk>/', LabTestAPIView.as_view(), name='labtest-detail'),
    path('labbills/', LabBillAPIView.as_view(), name='labbill-list'),
    path('labbills/<int:pk>/', LabBillAPIView.as_view(), name='labbill-detail'),
    path('lab-devices/', LabdeviceCreateApiView.as_view(), name='lab-device-list-create'),
    path('lab-devices/<int:pk>/', LabdeviceRetrieveUpdateView.as_view(), name='lab-device-retrieve-update'),
]