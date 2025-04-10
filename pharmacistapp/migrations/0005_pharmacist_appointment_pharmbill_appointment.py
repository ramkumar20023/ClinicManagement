# Generated by Django 5.1.7 on 2025-04-06 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceptionistApp', '0002_remove_batch_pharm_remove_consultation_appointment_and_more'),
        ('pharmacistapp', '0004_remove_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacist',
            name='Appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_orders', to='ReceptionistApp.appointment'),
        ),
        migrations.AddField(
            model_name='pharmbill',
            name='Appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_bills', to='ReceptionistApp.appointment'),
        ),
    ]
