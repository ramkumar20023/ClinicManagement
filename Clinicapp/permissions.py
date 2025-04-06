from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Doctor').exists()

class IsReceptionist(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Receptionist').exists()

class IsPharmacist(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Pharmacist').exists()
    
class IsLabTechnician(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Lab Technician').exists()

