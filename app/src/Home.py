##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('Pharmacogenetics App')
st.write('\n\n')
st.write('### HI! As which user would you like to interact with the app?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 

if st.button("Act as Dr. Emily Zhang, A Doctor", 
            type = 'primary', 
            use_container_width=True):
    # when user clicks the button, they are now considered authenticated
    st.session_state['authenticated'] = True
    # we set the role of the current user
    st.session_state['role'] = 'doctor'
    # we add the first name of the user (so it can be displayed on 
    # subsequent pages). 
    st.session_state['first_name'] = 'Emily'
    st.session_state['last_name'] = 'Zhang'
    # finally, we ask streamlit to switch to another page, in this case, the 
    # landing page for this particular user type
    logger.info("Logging in as Doctor Persona")
    st.switch_page('pages/01_doctor_home.py')

if st.button('Act as Sarah Johnson, a Patient', 
             type='primary', 
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'patient'
    st.session_state['first_name'] = 'Sarah'
    st.session_state['last_name'] = 'Johnson'
    logger.info("Logging in as Patient Persona")
    st.switch_page('pages/02_patient_home.py')

if st.button('Act as Jason Lee, an Data Analyst', 
             type='primary', 
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'analyst'
    st.session_state['first_name'] = 'Jason'
    st.session_state['last_name'] = 'Lee'
    logger.info("Logging in as Data Analyst Persona")
    st.switch_page('pages/03_analyst_home.py')

if st.button('Act as David Roberts, a System Administrator', 
             type='primary', 
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = 'David'
    st.session_state['last_name'] = 'Roberts'
    logger.info("Logging in as System Admin Persona")
    st.switch_page('pages/04_admin_home.py')