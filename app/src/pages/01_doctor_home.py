import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Dr. {st.session_state['last_name']}.")

st.write('')
st.write('### What would you like to do today?')

# Button to view the patient list
if st.button("View Patient List", type="primary", use_container_width=True):
        st.switch_page("pages/01_doctor_patient_list.py")

# Button to view medication alerts
if st.button("View Medication Alerts", type="primary", use_container_width=True):
    st.switch_page("pages/01_doctor_medication_alerts.py")

# Button to view patient data (such as genetic profile or treatment progress)
if st.button("View Patient Data", type="primary", use_container_width=True):
    st.switch_page("pages/01_doctor_view_data.py")