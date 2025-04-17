import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
from api.backend.db_connection.db_connection import db

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

# Fetch patient genetic profiles for the doctor
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT p.Name AS PatientName, g.TestDate, g.GeneticMarkers
    FROM GENETIC_PROFILE g
    JOIN PATIENT p ON g.PatientID = p.PatientID
""")
genetic_profiles = cursor.fetchall()

st.title(f"Patient Genetic Profiles for Dr. {st.session_state['first_name']}")

# Check if there are genetic profiles and display them
if genetic_profiles:
    for profile in genetic_profiles:
        st.write(f"**Patient Name**: {profile['PatientName']}")
        st.write(f"**Test Date**: {profile['TestDate']}")
        st.write(f"**Genetic Markers**: {profile['GeneticMarkers']}")
        st.write("-" * 50)
else:
    st.write("No genetic profiles found.")

# Option to go back to the doctor home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('01_doctor_home.py')