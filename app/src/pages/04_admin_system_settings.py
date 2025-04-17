import logging
logger = logging.getLogger(__name__)

import streamlit as st
from api.backend.db_connection.db_connection import db
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

if st.session_state.get('page') == 'system_settings':
    st.title(f"System Settings, {st.session_state['first_name']}")

    # Fetch system encryption settings
    cursor = db.get_db().cursor()
    cursor.execute("""
        SELECT Parameter, Value FROM ENCRYPTION_SETTINGS
    """)
    settings = cursor.fetchall()

    if settings:
        for setting in settings:
            st.write(f"**{setting['Parameter']}**: {setting['Value']}")
            st.write("-" * 50)
    else:
        st.write("No system settings found.")

    # Option to update encryption settings
    if st.button("Update Encryption Settings", type="primary", use_container_width=True):
        st.write("Updating Encryption Settings...")
        # Navigate to update encryption settings page (if you want to add more logic here)

# Option to go back to admin home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('04_admin_home.py')