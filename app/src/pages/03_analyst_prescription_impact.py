import logging
logger = logging.getLogger(__name__)

import streamlit as st
from api.backend.db_connection import db
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Fetch genetic data and prescription information
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT p.Name, g.GeneticMarkers, m.Name AS Medication, 
           m.DosageGuidelines, tp.SymptomScore
    FROM PATIENT p
    JOIN GENETIC_PROFILE g ON p.PatientID = g.PatientID
    JOIN PRESCRIPTION pr ON p.PatientID = pr.PatientID
    JOIN MEDICATION m ON pr.MedicationID = m.MedicationID
    JOIN TREATMENT_PROGRESS tp ON p.PatientID = tp.PatientID
    WHERE g.TestDate IS NOT NULL
""")

data = cursor.fetchall()

st.title(f"Genetic Impact on Medication Effectiveness")

if data:
    for record in data:
        st.write(f"**Patient Name**: {record['Name']}")
        st.write(f"**Genetic Markers**: {record['GeneticMarkers']}")
        st.write(f"**Medication**: {record['Medication']}")
        st.write(f"**Dosage Guidelines**: {record['DosageGuidelines']}")
        st.write(f"**Symptom Score**: {record['SymptomScore']}")
        st.write("-" * 50)
else:
    st.write("No data available for genetic impact on prescriptions.")

# Option to analyze further or view detailed reports
if st.button("Analyze Genetic Impact Further", type="primary", use_container_width=True):
    st.write("Analyze the genetic impact on a larger dataset of medications and symptoms.")

# Option to go back to analyst home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('03_analyst_home.py')