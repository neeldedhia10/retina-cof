# Generated by Django 4.2.4 on 2023-10-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retina', '0009_alter_patient_patient_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dme_status',
            field=models.CharField(default='', max_length=100),
        ),
    ]
