import streamlit as st

def email_ui(api_app):
    email_text = st.text_area("Enter Email Content")
    if st.button("Analyze Email"):
        response = api_app.test_client().post("/analyze/email", json={"content": email_text})
        st.write(response.json)
