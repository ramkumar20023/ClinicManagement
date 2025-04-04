# Generated by Django 5.1.7 on 2025-04-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacistapp', '0002_pharmbill_finalprice_pharmbill_gst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmbill',
            name='FinalPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pharmbill',
            name='TotalPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
