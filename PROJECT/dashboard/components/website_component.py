import streamlit as st

def website_ui(api_app):
    st.write("Upload website screenshot for analysis")
    image_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if st.button("Analyze Website") and image_file:
        response = api_app.test_client().post("/analyze/website", files={"file": image_file})
        st.write(response.json)
