import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
from api.backend.db_connection.db_connection import db

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Dr. {st.session_state['last_name']}")

# Show patient list for the doctor
st.write("### Your Patient List:")
doctor_id = st.session_state['doctor_id']  # Assume doctor_id is set in session state

# Query to get the list of patients for this doctor
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT p.PatientID, p.Name, p.Age, p.ContactInfo
    FROM PATIENT p
    JOIN PRESCRIPTION pr ON p.PatientID = pr.PatientID
    WHERE pr.DoctorID = %s
""", (doctor_id,))
patients = cursor.fetchall()

if patients:
    for patient in patients:
        st.write(f"**Patient Name:** {patient['Name']}")
        st.write(f"**Age:** {patient['Age']}")
        st.write(f"**Contact Info:** {patient['ContactInfo']}")
        st.write("-" * 50)
else:
    st.write("No patients found.")

# Option to view a specific patient's details
if st.button("View Patient Medication History", type="primary", use_container_width=True):
    st.switch_page('02_patient_medication_history.py')

# Option to go back to doctor home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('01_doctor_home.py')
