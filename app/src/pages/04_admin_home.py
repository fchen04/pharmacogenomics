import logging
logger = logging.getLogger(__name__)

import streamlit as st
from api.backend.db_connection import db
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

st.title(f"Welcome Admin, {st.session_state['first_name']}")

st.write('### What would you like to do today?')

# Button to navigate to Admin Dashboard
if st.button('Go to Admin Dashboard', type='primary', use_container_width=True):
    st.switch_page('04_admin_dash.py')

# Button to manage system users
if st.button('Manage System Users', type='primary', use_container_width=True):
    st.switch_page('04_admin_user_manage.py')

# Button to view system logs
if st.button('View System Logs', type='primary', use_container_width=True):
    st.switch_page('04_admin_system_settings.py')

# Button to manage encryption settings
if st.button('Manage Encryption Settings', type='primary', use_container_width=True):
    st.switch_page('04_admin_system_settings.py')
