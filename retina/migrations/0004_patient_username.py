# Generated by Django 4.2.4 on 2023-08-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retina', '0003_rename_url_patient_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='username',
            field=models.CharField(default='', max_length=150),
        ),
    ]
