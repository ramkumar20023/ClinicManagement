# Generated by Django 5.1.7 on 2025-04-06 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinicapp', '0008_remove_appointment_doctor_and_more'),
        ('labtechnicianApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='PatientDetails',
        ),
        migrations.RemoveField(
            model_name='labtestreport',
            name='Appointment',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='Appointment',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='Appointment',
        ),
        migrations.RemoveField(
            model_name='appointmentbill',
            name='Appointment',
        ),
        migrations.RemoveField(
            model_name='labtesting',
            name='Appointment',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='Pharm',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='LabTesting',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='Prescription',
        ),
        migrations.RemoveField(
            model_name='patienthistory',
            name='Consultation',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='labdepartment',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='UserId',
        ),
        migrations.RemoveField(
            model_name='labtest',
            name='LabDepartment',
        ),
        migrations.DeleteModel(
            name='LabDevice',
        ),
        migrations.RemoveField(
            model_name='labtesting',
            name='Test',
        ),
        migrations.RemoveField(
            model_name='labtestreport',
            name='LabTesting',
        ),
        migrations.RemoveField(
            model_name='labtestreport',
            name='LabTechnician',
        ),
        migrations.RemoveField(
            model_name='login',
            name='Role',
        ),
        migrations.RemoveField(
            model_name='login',
            name='Signup',
        ),
        migrations.RemoveField(
            model_name='staffmanage',
            name='Login',
        ),
        migrations.RemoveField(
            model_name='pharmacist',
            name='Pharm',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='Medicine',
        ),
        migrations.RemoveField(
            model_name='pharmbill',
            name='Pharmacist',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='Role',
        ),
        migrations.RemoveField(
            model_name='staffmanage',
            name='Role',
        ),
        migrations.AlterField(
            model_name='labtest',
            name='Technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conducted_tests', to='Clinicapp.staffmanage'),
        ),
        migrations.AlterField(
            model_name='labbill',
            name='LabTest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lab_bills', to='labtechnicianApp.labtest'),
        ),
        migrations.DeleteModel(
            name='PatientDetails',
        ),
        migrations.DeleteModel(
            name='AppointmentBill',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Consultation',
        ),
        migrations.DeleteModel(
            name='PatientHistory',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='LabDepartment',
        ),
        migrations.DeleteModel(
            name='LabTesting',
        ),
        migrations.DeleteModel(
            name='LabTestReport',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Pharm',
        ),
        migrations.DeleteModel(
            name='Prescription',
        ),
        migrations.DeleteModel(
            name='Pharmacist',
        ),
        migrations.DeleteModel(
            name='PharmBill',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='StaffManage',
        ),
    ]
