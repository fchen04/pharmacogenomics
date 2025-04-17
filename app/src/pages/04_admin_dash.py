import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
from api.backend.db_connection import db

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Admin: {st.session_state['first_name']} {st.session_state['last_name']}")

# Show system logs
st.write('### System Logs')
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT Timestamp, EventType, Message
    FROM SYSTEM_LOG
    ORDER BY Timestamp DESC LIMIT 10
""")
logs = cursor.fetchall()

if logs:
    for log in logs:
        st.write(f"**Timestamp:** {log['Timestamp']}")
        st.write(f"**Event Type:** {log['EventType']}")
        st.write(f"**Message:** {log['Message']}")
        st.write("-" * 50)
else:
    st.write("No recent system logs.")

# Option to manage users
if st.button("Manage Users", type="primary", use_container_width=True):
    st.switch_page('02_Admin_User_Management.py')

# Option to manage system settings
if st.button("System Settings", type="primary", use_container_width=True):
    st.switch_page('03_Admin_System_Settings.py')

# Option to go to other admin functionalities
if st.button("View Drug Interaction Management", type="primary", use_container_width=True):
    st.switch_page('04_Admin_Drug_Interactions.py')

if st.button("View Alerts", type="primary", use_container_width=True):
    st.switch_page('05_Admin_Alerts.py')
