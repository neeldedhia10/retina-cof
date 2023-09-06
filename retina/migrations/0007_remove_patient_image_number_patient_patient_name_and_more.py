# Generated by Django 4.2.3 on 2023-09-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retina', '0006_remove_patient_patient_name_patient_image_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='image_number',
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(default='def', max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.IntegerField(),
        ),
    ]