from django.urls import path
from .views import LabTestAPIView, LabBillAPIView

urlpatterns = [
    path('labtests/', LabTestAPIView.as_view(), name='labtest-list'),
    path('labtests/<int:pk>/', LabTestAPIView.as_view(), name='labtest-detail'),
    path('labbills/', LabBillAPIView.as_view(), name='labbill-list'),
    path('labbills/<int:pk>/', LabBillAPIView.as_view(), name='labbill-detail'),
]