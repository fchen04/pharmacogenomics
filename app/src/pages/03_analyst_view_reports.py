import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

st.title("Analyst Reports")

# Option to generate reports (this is an example; you can modify based on the actual functionality)
if st.button("Generate Genetic Report", type="primary", use_container_width=True):
    # Trigger the report generation for genetic analysis
    st.write("Generating Genetic Report...")

# Display generated reports (example)
st.write("### Generated Reports")
st.write("Genetic Trends Report")
st.write("Prescription Impact Report")

# Option to go back to analyst home page
if st.button("Back to Home", type="primary", use_container_width=True):
    st.switch_page('03_analyst_home.py')