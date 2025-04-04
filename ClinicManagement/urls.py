"""
URL configuration for ClinicManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.http import JsonResponse

=======
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
>>>>>>> origin/pharmacist

urlpatterns = [
    
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/',include('Clinicapp.urls')),
    path('api/', include('ReceptionistApp.urls')),  # API Routes
=======
    path('api/pharmacistapp/', include('pharmacistapp.urls')),  
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login URL
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token Refresh URL
>>>>>>> origin/pharmacist
]
