from django.contrib import admin
from .models import doctorinform,Prescription,Consultation,LabTestReport,PatientHistory

# Register your models here.
admin.site.register(doctorinform)
admin.site.register(Prescription)
admin.site.register(Consultation)
admin.site.register(LabTestReport)
admin.site.register(PatientHistory)