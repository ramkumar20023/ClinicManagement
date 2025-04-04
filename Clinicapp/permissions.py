# Add this to your views.py or create a new permissions.py file
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.Role.RoleName == 'Admin'

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.Role.RoleName == 'Doctor'
class IsReceptionist(BasePermission):
    def has_permission(self, request, view):
        return request.user.Role.RoleName == 'Receptionist'

class IsPharmacist(BasePermission):
    def has_permission(self, request, view):
        return request.user.Role.RoleName == 'Pharmacist'
    
class IsLabTechnician(BasePermission):
    def has_permission(self, request, view):
        return request.user.Role.RoleName == 'Lab Technician'

