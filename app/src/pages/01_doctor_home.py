import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Doctor, {st.session_state['first_name']}.")

st.write('')
st.write('### What would you like to do today?')

# Button to view patient's profile
if st.button('View Patient Profiles', type='primary', use_container_width=True):
    st.switch_page('pages/01_doctor_patient_view.py')

# Button to view medication recommendations
if st.button('Provide Medication Recommendations', type='primary', use_container_width=True):
    st.switch_page('pages/01_doctor_medication_Advice.py')
