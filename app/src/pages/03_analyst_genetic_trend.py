import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
from api.backend.db_connection.db_connection import db

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Genetic Data Trends and Medication Effectiveness")

# Show genetic trends analysis options
st.write('### Genetic Trends Analysis:')
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT gp.GeneticMarkers, COUNT(*) AS NumPatients, AVG(DATEDIFF(tp.Date, pr.Date)) AS AvgResponseTime
    FROM GENETIC_PROFILE gp
    JOIN PATIENT p ON gp.PatientID = p.PatientID
    JOIN PRESCRIPTION pr ON p.PatientID = pr.PatientID
    JOIN TREATMENT_PROGRESS tp ON p.PatientID = tp.PatientID
    GROUP BY gp.GeneticMarkers
""")
genetic_trends = cursor.fetchall()

if genetic_trends:
    for trend in genetic_trends:
        st.write(f"**Genetic Marker:** {trend['GeneticMarkers']}")
        st.write(f"**Number of Patients:** {trend['NumPatients']}")
        st.write(f"**Average Response Time (Days):** {trend['AvgResponseTime']}")
        st.write("-" * 50)
else:
    st.write("No genetic trends data found.")

# Option to view medication effectiveness
if st.button("View Medication Effectiveness", type="primary", use_container_width=True):
    st.switch_page('03_analyst_prescription_impact.py')

# Option to go back to analyst home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('03_analyst_home.py')
