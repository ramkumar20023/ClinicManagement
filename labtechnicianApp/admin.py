from django.contrib import admin
from .models import LabTest, LabBill
from .models import AvailableLabTest

# @admin.register(LabTest)
# class LabTestAdmin(admin.ModelAdmin):
#     list_display = ('LaboratoryId', 'TestName', 'ResultDate')
#     search_fields = ('TestName', 'Technician_FirstName', 'Technician_LastName')

# @admin.register(LabBill)
# class LabBillAdmin(admin.ModelAdmin):
#     list_display = ('LabBillId', 'TotalPrice', 'created_at')
#     search_fields = ('LabBillId',)

admin.site.register(LabTest)
admin.site.register(LabBill)
admin.site.register(AvailableLabTest)