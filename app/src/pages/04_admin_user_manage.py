import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)

# Set up page configuration
st.set_page_config(layout="wide")
SideBarLinks()

# API base URL
API_URL = "http://host.docker.internal:4000/api"

# Check if current page is user management
if st.session_state.get('page') == 'user_management':
    st.title(f"Manage System Users, {st.session_state['first_name']}")

    # Fetch all users from the API
    try:
        response = requests.get(f"{API_URL}/admin/users")
        response.raise_for_status()
        users = response.json()

        if users:
            for user in users:
                st.write(f"**Username**: {user['Username']}")
                st.write(f"**Role**: {user['RoleID']}")
                st.write("-" * 50)
        else:
            st.write("No users found.")
    except requests.exceptions.RequestException as e:
        st.error("Failed to fetch system users.")
        logger.error(f"User fetch request failed: {e}")

    # Add new user interface trigger
    if st.button("Add New User", type="primary", use_container_width=True):
        st.write("Form to add new users goes here...")
        # You can build or navigate to a form-based page for user creation

# Back button to admin home
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('04_admin_home.py')
