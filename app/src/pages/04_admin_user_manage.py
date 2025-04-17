import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
from api.backend.db_connection import db

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Admin User Management")

# Show the list of system users
cursor = db.get_db().cursor()
cursor.execute("""
    SELECT UserID, Username, RoleID FROM SYSTEM_USER
""")
users = cursor.fetchall()

if users:
    for user in users:
        st.write(f"**Username:** {user['Username']}")
        st.write(f"**RoleID:** {user['RoleID']}")
        st.write("-" * 50)
else:
    st.write("No users found.")

# Option to add a new user
if st.button("Add New User", type="primary", use_container_width=True):
    st.switch_page('06_Admin_Add_User.py')
