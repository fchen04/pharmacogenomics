import logging
logger = logging.getLogger(__name__)

import streamlit as st
from api.backend.db_connection.db_connection import db
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Admin, {st.session_state['first_name']}")

st.write('### What would you like to do today?')

# Button for managing system users
if st.button('Manage System Users', type='primary', use_container_width=True):
    # Option to manage system users (e.g., view, add, remove users)
    st.write("Manage users, assign roles, and update user details.")

    # Example: Fetch all users in the system
    cursor = db.get_db().cursor()
    cursor.execute("""
        SELECT UserID, Username, RoleID FROM SYSTEM_USER
    """)
    users = cursor.fetchall()

    if users:
        st.write("#### Current System Users")
        for user in users:
            st.write(f"**UserID**: {user['UserID']}")
            st.write(f"**Username**: {user['Username']}")
            st.write(f"**RoleID**: {user['RoleID']}")
            st.write("-" * 50)
    else:
        st.write("No users found in the system.")

# Button to view and manage system logs
if st.button('View System Logs', type='primary', use_container_width=True):
    # Option to view the system logs for auditing
    st.write("Here, the system logs are displayed to track actions and errors.")
    
    cursor = db.get_db().cursor()
    cursor.execute("""
        SELECT LogID, EventType, Message, Timestamp FROM SYSTEM_LOG
    """)
    logs = cursor.fetchall()

    if logs:
        st.write("#### System Logs")
        for log in logs:
            st.write(f"**LogID**: {log['LogID']}")
            st.write(f"**Event Type**: {log['EventType']}")
            st.write(f"**Message**: {log['Message']}")
            st.write(f"**Timestamp**: {log['Timestamp']}")
            st.write("-" * 50)
    else:
        st.write("No logs found.")

# Button to update and manage system settings (like encryption settings)
if st.button('Manage System Settings', type='primary', use_container_width=True):
    # Option to manage system-level configurations like encryption and data security
    st.write("View and modify encryption settings or other configurations related to system security.")
    
    cursor = db.get_db().cursor()
    cursor.execute("""
        SELECT Parameter, Value FROM ENCRYPTION_SETTINGS
    """)
    settings = cursor.fetchall()

    if settings:
        st.write("#### Current Encryption Settings")
        for setting in settings:
            st.write(f"**{setting['Parameter']}**: {setting['Value']}")
            st.write("-" * 50)
    else:
        st.write("No encryption settings found.")
    
    st.write("You can modify these settings to enhance data security.")

# Button to perform cleanup tasks (e.g., remove old records, clean data)
if st.button('Perform System Cleanup', type='primary', use_container_width=True):
    st.write("Perform maintenance tasks, like cleaning up inactive records or old logs.")
    
    cursor = db.get_db().cursor()
    cursor.execute("""
        SELECT TaskID, Description, ScheduledDate, Status FROM CLEANUP_TASK
    """)
    tasks = cursor.fetchall()

    if tasks:
        st.write("#### Pending Cleanup Tasks")
        for task in tasks:
            st.write(f"**TaskID**: {task['TaskID']}")
            st.write(f"**Description**: {task['Description']}")
            st.write(f"**Scheduled Date**: {task['ScheduledDate']}")
            st.write(f"**Status**: {task['Status']}")
            st.write("-" * 50)
    else:
        st.write("No cleanup tasks are currently scheduled.")

# Provide option to navigate to other admin pages
if st.button("Navigate to Admin User Management", type="primary", use_container_width=True):
    st.write("Redirecting to user management page for additional admin tasks.")
    # Implement navigation to another page where the admin can manage users
    # For example: st.switch_page('admin_user_management.py')

# Option to go back to admin home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('04_admin_home.py')