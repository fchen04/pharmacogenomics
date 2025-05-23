import logging
logger = logging.getLogger(__name__)

import streamlit as st
from api.backend.db_connection import db
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Fetch the genetic profile and medication recommendations for the patient
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT p.Name, g.TestDate, g.GeneticMarkers, m.Name AS Medication, m.DosageGuidelines
    FROM PATIENT p
    JOIN GENETIC_PROFILE g ON p.PatientID = g.PatientID
    JOIN MEDICATION_RECOMMENDATION mr ON p.PatientID = mr.PatientID
    JOIN MEDICATION m ON mr.MedicationID = m.MedicationID
    WHERE p.PatientID = %s
""", (st.session_state["patient_id"],))  # Assuming session state stores the patient ID

genetic_data = cursor.fetchall()

st.title(f"Welcome {st.session_state['first_name']} to your Genetic Profile and Medication Recommendations!")

if genetic_data:
    for record in genetic_data:
        st.write(f"**Test Date**: {record['TestDate']}")
        st.write(f"**Genetic Markers**: {record['GeneticMarkers']}")
        st.write(f"**Medication Recommendation**: {record['Medication']}")
        st.write(f"**Dosage Guidelines**: {record['DosageGuidelines']}")
else:
    st.write("No genetic data or medication recommendations found.")

# Option to update genetic profile or ask for new recommendations
if st.button("Update My Genetic Profile", type="primary", use_container_width=True):
    st.write("Please contact your healthcare provider for genetic testing.")

# Option to go back to the patient home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('02_patient_home.py')