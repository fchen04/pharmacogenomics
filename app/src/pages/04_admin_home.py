import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Admin, {st.session_state['first_name']}.")

st.write('')
st.write('### What would you like to do today?')

# Button to manage users
if st.button('Manage System Users', type='primary', use_container_width=True):
    st.switch_page('pages/01_Admin_Manage_Users.py')

# Button to view logs and perform admin tasks
if st.button('View System Logs', type='primary', use_container_width=True):
    st.switch_page('pages/02_Admin_System_Logs.py')

# Button to manage ML models
if st.button('Manage ML Models', type='primary', use_container_width=True):
    st.switch_page('pages/03_Admin_ML_Models.py')
