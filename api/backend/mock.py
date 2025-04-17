import csv
from faker import Faker
import random
import os
from backend.rest_entry import get_db_connection  # Importing the connection function from rest_entry.py

# Initialize Faker
fake = Faker()

# Define number of rows to generate for each table
NUM_DOCTORS = 30
NUM_PATIENTS = 30
NUM_MEDICATIONS = 30
NUM_GENETIC_PROFILES = 50
NUM_PRESCRIPTIONS = 50
NUM_DRUG_INTERACTIONS = 25
NUM_ALERTS = 30
NUM_TREATMENT_PROGRESS = 50
NUM_MEDICATION_RECOMMENDATIONS = 50

# Generate data based on tables in PharmacogeneticAppDB
def generate_doctors():
    return [(fake.name(), fake.job()) for _ in range(NUM_DOCTORS)]

def generate_patients():
    return [(fake.name(), fake.random_int(min=20, max=80), fake.email()) for _ in range(NUM_PATIENTS)]

def generate_medications():
    return [(fake.word(), fake.text(), fake.text()) for _ in range(NUM_MEDICATIONS)]

def generate_genetic_profiles():
    return [(random.randint(1, NUM_PATIENTS), fake.date(), fake.text(), random.randint(1, 5)) for _ in range(NUM_GENETIC_PROFILES)]

def generate_prescriptions():
    return [(random.randint(1, NUM_PATIENTS), random.randint(1, NUM_DOCTORS), random.randint(1, NUM_MEDICATIONS), fake.date()) for _ in range(NUM_PRESCRIPTIONS)]

def generate_drug_interactions():
    return [(random.randint(1, NUM_MEDICATIONS), random.randint(1, NUM_MEDICATIONS), fake.text()) for _ in range(NUM_DRUG_INTERACTIONS)]

def generate_alerts():
    return [(random.randint(1, NUM_PATIENTS), fake.word(), fake.text(), fake.date()) for _ in range(NUM_ALERTS)]

def generate_treatment_progress():
    return [(random.randint(1, NUM_PATIENTS), fake.date(), fake.word(), fake.text()) for _ in range(NUM_TREATMENT_PROGRESS)]

def generate_medication_recommendations():
    return [(random.randint(1, NUM_PATIENTS), random.randint(1, NUM_MEDICATIONS), fake.date()) for _ in range(NUM_MEDICATION_RECOMMENDATIONS)]

# Insert data into MySQL database
def insert_data(table_name, data):
    connection = get_db_connection()  # Use the connection function from rest_entry.py
    cursor = connection.cursor()
    if table_name == "DOCTOR":
        cursor.executemany("INSERT INTO DOCTOR (Name, Specialty) VALUES (%s, %s)", data)
    elif table_name == "PATIENT":
        cursor.executemany("INSERT INTO PATIENT (Name, Age, ContactInfo) VALUES (%s, %s, %s)", data)
    elif table_name == "MEDICATION":
        cursor.executemany("INSERT INTO MEDICATION (Name, Indications, DosageGuidelines) VALUES (%s, %s, %s)", data)
    elif table_name == "GENETIC_PROFILE":
        cursor.executemany("INSERT INTO GENETIC_PROFILE (PatientID, TestDate, GeneticMarkers, SourceID) VALUES (%s, %s, %s, %s)", data)
    elif table_name == "PRESCRIPTION":
        cursor.executemany("INSERT INTO PRESCRIPTION (PatientID, DoctorID, MedicationID, Date) VALUES (%s, %s, %s, %s)", data)
    elif table_name == "DRUG_INTERACTION":
        cursor.executemany("INSERT INTO DRUG_INTERACTION (Medication1ID, Medication2ID, InteractionDetails) VALUES (%s, %s, %s)", data)
    elif table_name == "ALERT":
        cursor.executemany("INSERT INTO ALERT (PatientID, AlertType, Message, Date) VALUES (%s, %s, %s, %s)", data)
    elif table_name == "TREATMENT_PROGRESS":
        cursor.executemany("INSERT INTO TREATMENT_PROGRESS (PatientID, Date, SymptomScore, LabResults) VALUES (%s, %s, %s, %s)", data)
    elif table_name == "MEDICATION_RECOMMENDATION":
        cursor.executemany("INSERT INTO MEDICATION_RECOMMENDATION (PatientID, MedicationID, Date) VALUES (%s, %s, %s)", data)

    connection.commit()
    cursor.close()
    connection.close()

# Generate and insert all data
def generate_and_insert_data():
    doctor_data = generate_doctors()
    insert_data("DOCTOR", doctor_data)
    
    patient_data = generate_patients()
    insert_data("PATIENT", patient_data)
    
    medication_data = generate_medications()
    insert_data("MEDICATION", medication_data)
    
    genetic_profile_data = generate_genetic_profiles()
    insert_data("GENETIC_PROFILE", genetic_profile_data)
    
    prescription_data = generate_prescriptions()
    insert_data("PRESCRIPTION", prescription_data)
    
    drug_interaction_data = generate_drug_interactions()
    insert_data("DRUG_INTERACTION", drug_interaction_data)
    
    alert_data = generate_alerts()
    insert_data("ALERT", alert_data)
    
    treatment_progress_data = generate_treatment_progress()
    insert_data("TREATMENT_PROGRESS", treatment_progress_data)
    
    medication_recommendation_data = generate_medication_recommendations()
    insert_data("MEDICATION_RECOMMENDATION", medication_recommendation_data)

# Run mock data generation and insertion
generate_and_insert_data()

