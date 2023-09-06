# Import necessary modules
import os
import django
from retina.models import Patient
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cof.settings')

django.setup()

patients = Patient.objects.all()

# Update fields for each patient
for patient in patients:
    patient.dr_type = ''
    patient.username = ''
    patient.is_processed = False  # Set to default value
    patient.under_process = False  # Set to default value
    patient.save()  # Save changes to the database



        