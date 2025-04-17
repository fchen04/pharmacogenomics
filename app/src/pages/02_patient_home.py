import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Patient, {st.session_state['first_name']}.")

st.write('')
st.write('### What would you like to do today?')

# Button to view medication history
if st.button('View My Medication History', type='primary', use_container_width=True):
    st.switch_page('pages/02_patient_medication_history.py')

# Button to view progress monitoring
if st.button('Track My Treatment Progress', type='primary', use_container_width=True):
    st.switch_page('pages/02_patient_progress.py')
