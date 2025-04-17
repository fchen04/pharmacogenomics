import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

st.title("Welcome, Analyst!")

# Buttons for different analyst functionalities
st.write('### What would you like to do today?')

# Button to view genetic trends
if st.button("View Genetic Trends", type="primary", use_container_width=True):
    # When clicked, switch to the genetic trends page
    st.switch_page("pages/03_analyst_genetic_trend.py")

# Button to view prescription impact
if st.button("View Prescription Impact", type="primary", use_container_width=True):
    # When clicked, switch to the prescription impact page
    st.switch_page("pages/03_analyst_prescription_impact.py")

# Button to view reports
if st.button("View Reports", type="primary", use_container_width=True):
    # When clicked, switch to the reports page
    st.switch_page("pages/03_analyst_view_reports.py")
