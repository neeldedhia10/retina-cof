from django.db import models
from django.core.validators import int_list_validator


class Patient(models.Model):
    patient_name = models.CharField(max_length=255, primary_key=False,default='def')
    patient_id = models.CharField(max_length=10, primary_key=True)
    link = models.CharField(max_length=500, default='')
    username = models.CharField(max_length=150,default='')
    is_processed = models.BooleanField(default=False)
    under_process = models.BooleanField(default=False)
    dr_type = models.CharField(max_length=100, default='')
    dme_status = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.patient_id
