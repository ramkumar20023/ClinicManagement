from django.urls import path
from .views import PharmacistAPIView, PharmBillAPIView

urlpatterns = [
    path('pharmacist', PharmacistAPIView.as_view(), name='pharmacist-list'),  # For listing and creation
    path('pharmacist/<int:pk>/', PharmacistAPIView.as_view(), name='pharmacist-detail'),  # For single pharmacist
    path('bills/', PharmBillAPIView.as_view(), name='pharmbill-list'),  # For bills listing
    path('bills/<int:pk>/', PharmBillAPIView.as_view(), name='pharmbill-detail'),  # For single bill
]