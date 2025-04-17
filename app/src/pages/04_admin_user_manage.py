import logging
logger = logging.getLogger(__name__)

import streamlit as st
from api.backend.db_connection import db
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

if st.session_state.get('page') == 'user_management':
    st.title(f"Manage System Users, {st.session_state['first_name']}")

    # Fetch all users from the database
    cursor = db.get_db().cursor()
    cursor.execute("""
        SELECT * FROM SYSTEM_USER
    """)
    users = cursor.fetchall()

    if users:
        for user in users:
            st.write(f"**Username**: {user['Username']}")
            st.write(f"**Role**: {user['RoleID']}")
            st.write("-" * 50)
    else:
        st.write("No users found.")

    # Option to add new user or manage existing ones
    if st.button("Add New User", type="primary", use_container_width=True):
        st.write("Form to add new users goes here...")
        # You can implement a form to add a new user here or navigate to another page for that.

# Option to go back to admin home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('04_admin_home.py')