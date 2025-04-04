from django.urls import path
from .views import PharmacistAPIView, PharmBillAPIView

urlpatterns = [
    path('pharmacists/', PharmacistAPIView.as_view(), name='pharmacist-list'),
    path('pharmacists/<int:pk>/', PharmacistAPIView.as_view(), name='pharmacist-detail'),
    path('pharmbills/', PharmBillAPIView.as_view(), name='pharmbill-list'),
    path('pharmbills/<int:pk>/', PharmBillAPIView.as_view(), name='pharmbill-detail'),
]