import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
from api.backend.db_connection import db

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Treatment Progress for Patient: {st.session_state['first_name']} {st.session_state['last_name']}")

# Fetch the patient's treatment progress from the database
patient_id = st.session_state['patient_id']  # Assume patient_id is set in session state

# Query to get the treatment progress
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT tp.Date, tp.SymptomScore, tp.LabResults
    FROM TREATMENT_PROGRESS tp
    WHERE tp.PatientID = %s
    ORDER BY tp.Date DESC
""", (patient_id,))
progress_data = cursor.fetchall()

# Display the treatment progress
if progress_data:
    st.write("### Your Treatment Progress:")
    for progress in progress_data:
        st.write(f"**Date:** {progress['Date']}")
        st.write(f"**Symptom Score:** {progress['SymptomScore']}")
        st.write(f"**Lab Results:** {progress['LabResults']}")
        st.write("-" * 50)
else:
    st.write("No treatment progress data found.")

# Option to go back to the patient home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('00_Patient_Home.py')
