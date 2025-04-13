# Generated by Django 5.1.7 on 2025-04-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceptionistApp', '0002_remove_batch_pharm_remove_consultation_appointment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetails',
            name='RegNo',
            field=models.IntegerField(help_text='Medical Record Number', null=True, unique=True, verbose_name='MR No'),
        ),
    ]
