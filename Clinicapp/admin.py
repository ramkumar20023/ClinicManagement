from django.contrib import admin
from .models import Doctor,StaffManage,Pharm,LabDevice,Role,Department,Batch

# Register your models here.
admin.site.register(Role)
# admin.site.register(Signup)
# admin.site.register(Login)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(StaffManage)
admin.site.register(Pharm)
admin.site.register(Batch)
admin.site.register(LabDevice)