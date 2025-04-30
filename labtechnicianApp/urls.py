from django.urls import path
from .views import LabTestAPIView, LabBillAPIView,LabdeviceCreateApiView, LabdeviceRetrieveUpdateView,LabtechnicianDashboard
from .views import SignupAPIView, LoginAPIView
from .views import update_labdevice_status

from .views import AvailableLabTestListCreateView
from .views import AvailableLabTestRetrieveUpdateView


urlpatterns = [
    path('labtests/', LabTestAPIView.as_view(), name='labtest-list'),
    path('labtests/<int:pk>/', LabTestAPIView.as_view(), name='labtest-detail'),
    path('labbills/', LabBillAPIView.as_view(), name='labbill-list'),
    path('labbills/<int:pk>/', LabBillAPIView.as_view(), name='labbill-detail'),
    path('devices/', LabdeviceCreateApiView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', LabdeviceRetrieveUpdateView.as_view(), name='device-retrieve-update'),
    path('labdashboard/', LabtechnicianDashboard.as_view(), name='labtechnician-dashboard'),
    path("signup/", SignupAPIView.as_view(),name="user-signup"),
    path("login/",LoginAPIView.as_view(),name="user-login"),
    path('labdevices/<int:pk>/update-status/', update_labdevice_status, name='update-labdevice-status'),

    path('labtest/', AvailableLabTestListCreateView.as_view(), name='available-lab-tests'),
    path('labtest/<int:pk>/', AvailableLabTestRetrieveUpdateView.as_view(), name='available-lab-test-detail'),

]