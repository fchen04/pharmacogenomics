import logging
logger = logging.getLogger(__name__)

import streamlit as st
from api.backend.db_connection.db_connection import db
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Fetch medication alerts for the doctor
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT p.Name AS PatientName, a.AlertType, a.Message, a.Date, m.Name AS MedicationName
    FROM ALERT a
    JOIN PATIENT p ON a.PatientID = p.PatientID
    JOIN PRESCRIPTION pr ON pr.PatientID = p.PatientID
    JOIN MEDICATION m ON pr.MedicationID = m.MedicationID
    WHERE a.AlertType = 'Drug Interaction'
""")

alerts = cursor.fetchall()

st.title(f"Medication Alerts for Dr. {st.session_state['last_name']}")

if alerts:
    for alert in alerts:
        st.write(f"**Patient**: {alert['PatientName']}")
        st.write(f"**Medication**: {alert['MedicationName']}")
        st.write(f"**Alert Type**: {alert['AlertType']}")
        st.write(f"**Message**: {alert['Message']}")
        st.write(f"**Date**: {alert['Date']}")
        st.write("-" * 50)
else:
    st.write("No medication alerts found.")

# Additional section for doctors to review more details about medication interactions
st.write("### Medication Interaction Advice")

# Button to review a more comprehensive medication interaction report
if st.button("Review Full Medication Interaction Details", type="primary", use_container_width=True):
    # Fetch more detailed information about drug interactions
    cursor.execute("""
        SELECT m1.Name AS Medication1, m2.Name AS Medication2, di.InteractionDetails
        FROM DRUG_INTERACTION di
        JOIN MEDICATION m1 ON di.Medication1ID = m1.MedicationID
        JOIN MEDICATION m2 ON di.Medication2ID = m2.MedicationID
    """)
    
    interactions = cursor.fetchall()

    if interactions:
        st.write("### Full Medication Interaction Details")
        for interaction in interactions:
            st.write(f"**Medication 1**: {interaction['Medication1']}")
            st.write(f"**Medication 2**: {interaction['Medication2']}")
            st.write(f"**Interaction Details**: {interaction['InteractionDetails']}")
            st.write("-" * 50)
    else:
        st.write("No detailed drug interaction information found.")
    
    st.write("You can use this information to make informed decisions about the patient's medication regimen.")

# Option to go back to the doctor home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('01_doctor_home.py')