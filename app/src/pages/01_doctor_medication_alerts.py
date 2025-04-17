import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Define API base URL
API_BASE_URL = "http://host.docker.internal:4000/api"

# Function to fetch medication alerts from the API
def fetch_medication_alerts():
    try:
        response = requests.get(f"{API_BASE_URL}/doctor/alerts")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching medication alerts: {e}")
        return []

# Fetch medication alerts for the doctor
alerts = fetch_medication_alerts()

st.title(f"Medication Alerts for Dr. {st.session_state['last_name']}")

# Display alerts if available
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
    try:
        response = requests.get(f"{API_BASE_URL}/doctor/drug_interactions")
        response.raise_for_status()
        interactions = response.json()

        if interactions:
            st.write("### Full Medication Interaction Details")
            for interaction in interactions:
                st.write(f"**Medication 1**: {interaction['Medication1']}")
                st.write(f"**Medication 2**: {interaction['Medication2']}")
                st.write(f"**Interaction Details**: {interaction['InteractionDetails']}")
                st.write("-" * 50)
        else:
            st.write("No detailed drug interaction information found.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching drug interactions: {e}")

    st.write("You can use this information to make informed decisions about the patient's medication regimen.")

# Option to go back to the doctor home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('01_doctor_home.py')