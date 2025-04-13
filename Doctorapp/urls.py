from django.urls import path
from .views import (DoctorinformCreateApiview, DoctorinformReteriveupdateApiview,
                    PrescriptioncreateApiview,PrescriptionRetrieveupdateApiview,
                    ConsulationcreateApiview,ConsulatntRetrieveupdateApiview,
                    LabtestReportCreateApiview,LabtestRetrieveupdateApiview,
                    PatienthistorycreateApiview, PatienthistoryRetrieveupdateview)

urlpatterns=[
    path('doctorinform/', DoctorinformCreateApiview.as_view(), name='doctor-information'),
    path('doctorinform/<int:pk>/', DoctorinformReteriveupdateApiview.as_view(), name='information-details'),

    path('prescription/',PrescriptioncreateApiview.as_view(), name='prescription-list'),
    path('prescription/<int:pk>/', PrescriptionRetrieveupdateApiview.as_view(), name='prescription-detail'),

    path('consultation/', ConsulationcreateApiview.as_view(), name='consultation-list'),
    path('consultation/<int:pk>/', ConsulatntRetrieveupdateApiview.as_view(), name='consultation-detail'),

    path('testreport/', LabtestReportCreateApiview.as_view(), name='labtestreport-list'),
    path('testreport/<int:pk>/', LabtestRetrieveupdateApiview.as_view(), name='labtestreport-detail'),

    path('patienthistory/', PatienthistorycreateApiview.as_view(), name='patienthistory=list'),
    path('patienthistory/<int:pk>', PatienthistoryRetrieveupdateview.as_view(), name='patienthistory-detail')
]