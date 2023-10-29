import csv
from retina.models import Patient
from django.db import transaction
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cof.settings')

# Path to your CSV file
csv_file_path = 'scripts/shuffled_file.csv'
Patient.objects.all().delete()
# Read the CSV file and populate data
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    with transaction.atomic():
        for row in reader:
            if len(row) >= 2:
                patient_name = row[0]
                link = row[2]
                patient_id = row[1]

                # Check if a record with the same patient_id exists
                existing_patient = Patient.objects.filter(
                    patient_id=patient_id).first()

                if existing_patient:
                    # Update the existing record if needed
                    existing_patient.link = link
                    existing_patient.patient_id = patient_id
                    existing_patient.save()
                else:
                    # Create a new Patient instance and save it to the database
                    Patient.objects.create(
                        patient_id=patient_id,
                        link=link,
                        patient_name = patient_name
                    )

print("Database updated successfully.")
