from flask import Blueprint, request, jsonify, make_response, current_app
from db_connection import db

# Create a new Blueprint object for doctor routes
doctors = Blueprint("doctors", __name__)

# ------------------------------------------------------------
# Get patient medication recommendations 
@doctors.route("/patients/<int:patient_id>/medications", methods=["GET"])
def get_patient_medications(patient_id):
    current_app.logger.info(f"GET /patients/{patient_id}/medications route")
    cursor = db.get_db().cursor()
    cursor.execute("""
        SELECT r.RecommendationID, r.PatientID, r.MedicationID, m.Name AS Medication, r.Date
        FROM MEDICATION_RECOMMENDATION r
        JOIN MEDICATION m ON r.MedicationID = m.MedicationID
        WHERE r.PatientID = %s
    """, (patient_id,))
    medications = cursor.fetchall()
    response = make_response(jsonify(medications))
    response.status_code = 200
    return response


# ------------------------------------------------------------
# Add a new drug interaction 
@doctors.route("/drug_interactions", methods=["POST"])
def add_drug_interaction():
    current_app.logger.info("POST /drug_interactions route")
    data = request.get_json()
    medication1_id = data.get('medication1_id')
    medication2_id = data.get('medication2_id')
    interaction_details = data.get('interaction_details')

    cursor = db.get_db().cursor()
    cursor.execute("""
        INSERT INTO DRUG_INTERACTION (Medication1ID, Medication2ID, InteractionDetails)
        VALUES (%s, %s, %s)
    """, (medication1_id, medication2_id, interaction_details))
    db.get_db().commit()

    response = make_response(jsonify({"message": "Drug interaction added."}))
    response.status_code = 201
    return response


# ------------------------------------------------------------
# Update a patient's treatment progress 
@doctors.route("/patients/<int:patient_id>/progress", methods=["PUT"])
def update_patient_progress(patient_id):
    current_app.logger.info(f"PUT /patients/{patient_id}/progress route")
    data = request.get_json()
    symptom_score = data.get('symptom_score')
    lab_results = data.get('lab_results')

    cursor = db.get_db().cursor()
    cursor.execute("""
        UPDATE TREATMENT_PROGRESS 
        SET SymptomScore = %s, LabResults = %s
        WHERE PatientID = %s
    """, (symptom_score, lab_results, patient_id))
    db.get_db().commit()

    response = make_response(jsonify({"message": "Patient progress updated."}))
    response.status_code = 200
    return response
