import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
The goal of this demo is to provide a comprehensive platform for analyzing pharmacogenetic data. It aims to help patients, healthcare providers, and researchers make better medication decisions based on genetic information. The app offers functionalities such as:

- Medication recommendations based on genetic profiles.
- Drug interaction and side effect alerts.
- Patient progress tracking with genetic insights.

### Tech Stack

This project utilizes the following technologies:

- **Flask**: For building the REST API and handling backend logic.
- **Streamlit**: For building interactive front-end interfaces.
- **MySQL**: To manage and query the database, storing patient, medication, and genetic data.
- **Docker**: For containerizing the app, making it easy to run in different environments.

### Features Demonstrated

In this demo, the app showcases the following:

1. **Patient and Medication Data Management**: Allow users to view and update patient profiles, medications, and genetic profiles.
2. **Drug Interaction Alerts**: Display warnings about potential harmful drug interactions based on genetic data.
3. **Personalized Medication Recommendations**: Provide users with personalized medication suggestions based on their genetic markers.
4. **Admin Panel**: A system for administrators to manage user roles and view logs for maintaining system integrity.

### Future Features

Stay tuned for more updates and features to come, including advanced genetic data analytics and further integration with healthcare systems.

### How to Use

1. Set up the Docker containers using the provided `docker-compose.yaml` file.
2. Run the Flask API and Streamlit frontend.
3. Log in as one of the predefined users (Admin, Doctor, Analyst, or Patient) to explore the app’s functionalities.
    """
        )
