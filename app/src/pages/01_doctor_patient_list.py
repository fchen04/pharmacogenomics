import logging
import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd
import requests

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Set the title for the doctor
st.title(f"Welcome Dr. {st.session_state['last_name']}")

# Show patient list for the doctor
st.write("### Your Patient List:")
doctor_id = st.session_state['doctor_id']  # Assume doctor_id is set in session state

# API base URL
API_URL = "http://host.docker.internal:4000/api" 

# Fetch list of patients for this doctor from the API
try:
    response = requests.get(f"{API_URL}/doctor/{doctor_id}/patients")
    response.raise_for_status()
    patients_data = pd.DataFrame(response.json())

    if not patients_data.empty:
        for _, patient in patients_data.iterrows():
            st.write(f"**Patient Name:** {patient['Name']}")
            st.write(f"**Age:** {patient['Age']}")
            st.write(f"**Contact Info:** {patient['ContactInfo']}")
            st.write("-" * 50)
    else:
        st.write("No patients found.")
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching patient data: {e}")

# Option to view a specific patient's medication history
if st.button("View Patient Medication History", type="primary", use_container_width=True):
    st.switch_page('02_patient_medication_history.py')

# Option to go back to the doctor home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('01_doctor_home.py')
