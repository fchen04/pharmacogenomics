from flask import Blueprint, request, jsonify, make_response, current_app
from db_connection import db

# Create a new Blueprint object for analyst routes
analysts = Blueprint("analysts", __name__)

# ------------------------------------------------------------
# Get medication effectiveness across genetic markers 
@analysts.route("/medication-effectiveness", methods=["GET"])
def get_medication_effectiveness():
    current_app.logger.info("GET /medication-effectiveness route")
    cursor = db.get_db().cursor()
    cursor.execute("""
        SELECT gp.GeneticMarkers, COUNT(*) AS NumPatients, 
               AVG(DATEDIFF(tp.Date, pr.Date)) AS AvgResponseTime
        FROM GENETIC_PROFILE gp
        JOIN PATIENT p ON gp.PatientID = p.PatientID
        JOIN PRESCRIPTION pr ON p.PatientID = pr.PatientID
        JOIN TREATMENT_PROGRESS tp ON p.PatientID = tp.PatientID
        GROUP BY gp.GeneticMarkers
    """)
    effectiveness = cursor.fetchall()
    response = make_response(jsonify(effectiveness))
    response.status_code = 200
    return response


# ------------------------------------------------------------
# Get medication side effects based on genetic markers
@analysts.route("/medication-side-effects", methods=["GET"])
def get_medication_side_effects():
    current_app.logger.info("GET /medication-side-effects route")
    cursor = db.get_db().cursor()
    cursor.execute("""
        SELECT gp.GeneticMarkers, m.Name AS Medication, COUNT(pr.PrescriptionID) AS ReactionCount
        FROM PRESCRIPTION pr
        JOIN PATIENT p ON pr.PatientID = p.PatientID
        JOIN GENETIC_PROFILE gp ON p.PatientID = gp.PatientID
        JOIN MEDICATION m ON pr.MedicationID = m.MedicationID
        WHERE pr.SideEffectsReported IS NOT NULL
        GROUP BY gp.GeneticMarkers, m.MedicationID
    """)
    side_effects = cursor.fetchall()
    response = make_response(jsonify(side_effects))
    response.status_code = 200
    return response
