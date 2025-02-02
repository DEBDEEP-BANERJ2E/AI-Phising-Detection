import streamlit as st
from dashboard.components.email_component import email_ui
from dashboard.components.url_component import url_ui
from dashboard.components.website_component import website_ui

def run_dashboard(api_app):
    st.title("AI-Powered Phishing Detection System")

    option = st.sidebar.selectbox("Choose Analysis Type", ["Email", "URL", "Website"])

    if option == "Email":
        email_ui(api_app)
    elif option == "URL":
        url_ui(api_app)
    elif option == "Website":
        website_ui(api_app)
