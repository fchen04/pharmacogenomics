import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
from api.backend.db_connection.db_connection import db

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Medication History for Patient: {st.session_state['first_name']} {st.session_state['last_name']}")

# Fetch the patient's medication history from the database
patient_id = st.session_state['patient_id']  # Assume patient_id is set in session state

# Query to get the medication history
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT m.Name AS Medication, p.Date AS PrescriptionDate, m.DosageGuidelines, p.Date
    FROM PRESCRIPTION p
    JOIN MEDICATION m ON p.MedicationID = m.MedicationID
    WHERE p.PatientID = %s
""", (patient_id,))
medications = cursor.fetchall()

# Display the medication history
if medications:
    st.write("### Your Medication History:")
    for med in medications:
        st.write(f"**Medication:** {med['Medication']}")
        st.write(f"**Dosage Guidelines:** {med['DosageGuidelines']}")
        st.write(f"**Prescription Date:** {med['PrescriptionDate']}")
        st.write("-" * 50)
else:
    st.write("No medication history found.")

# Option to go back to the patient home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('02_patient_home.py')
