import streamlit as st

def url_ui(api_app):
    url = st.text_input("Enter URL")
    if st.button("Analyze URL"):
        response = api_app.test_client().post("/analyze/url", json={"url": url})
        st.write(response.json)
