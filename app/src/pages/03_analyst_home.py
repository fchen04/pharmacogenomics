import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
from api.backend.db_connection import db

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"System Settings")

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
    st.switch_page('07_Admin_Update_Encryption.py')
