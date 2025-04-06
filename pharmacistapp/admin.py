from django.contrib import admin
from .models import Pharmacist, PharmBill


@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display = ('PharmId', 'MedicineName', 'Quantity', 'PricePerUnit')
    search_fields = ('MedicineName',)

@admin.register(PharmBill)
class PharmBillAdmin(admin.ModelAdmin):
    list_display = ('BillId', 'TotalPrice', 'Created_at')
    search_fields = ('BillId',)

