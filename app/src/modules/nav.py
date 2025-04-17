# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


#### ------------------------ Admin Role ------------------------
def AdminHomeNav():
    st.sidebar.page_link("pages/00_Admin_Home.py", label="Admin Home", icon="👩‍💻")


def AdminManageUsersNav():
    st.sidebar.page_link("pages/01_Admin_Manage_Users.py", label="Manage Users", icon="👨‍⚖️")


#### ------------------------ Analyst Role ------------------------
def AnalystHomeNav():
    st.sidebar.page_link("pages/00_Analyst_Home.py", label="Analyst Home", icon="📊")


def AnalystReportsNav():
    st.sidebar.page_link("pages/01_Analyst_Reports.py", label="View Reports", icon="📈")


def AnalystTrendsNav():
    st.sidebar.page_link("pages/02_Analyst_Trends.py", label="Genetic Trends", icon="🔬")


#### ------------------------ Doctor Role ------------------------
def DoctorHomeNav():
    st.sidebar.page_link("pages/00_Doctor_Home.py", label="Doctor Home", icon="🩺")


def DoctorPatientViewNav():
    st.sidebar.page_link("pages/01_Doctor_Patient_View.py", label="Patient View", icon="👩‍⚕️")


def DoctorMedicationNav():
    st.sidebar.page_link("pages/02_Doctor_Medication_Advice.py", label="Medication Advice", icon="💊")


#### ------------------------ Patient Role ------------------------
def PatientHomeNav():
    st.sidebar.page_link("pages/00_Patient_Home.py", label="Patient Home", icon="👨‍⚕️")


def PatientMedicationNav():
    st.sidebar.page_link("pages/01_Patient_Medication_History.py", label="Medication History", icon="💊")


def PatientProgressNav():
    st.sidebar.page_link("pages/02_Patient_Progress.py", label="Progress Monitoring", icon="📊")


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

      # Show the Admin links if the user is an administrator
        if st.session_state["role"] == "admin":
            AdminHomeNav()
            AdminManageUsersNav()

        # If the user role is analyst, show the Analyst-specific pages
        if st.session_state["role"] == "analyst":
            AnalystHomeNav()
            AnalystReportsNav()
            AnalystTrendsNav()

        # If the user role is doctor, show doctor-specific pages
        if st.session_state["role"] == "doctor":
            DoctorHomeNav()
            DoctorPatientViewNav()
            DoctorMedicationNav()

        # If the user role is patient, show patient-specific pages
        if st.session_state["role"] == "patient":
            PatientHomeNav()
            PatientMedicationNav()
            PatientProgressNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
