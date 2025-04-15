import streamlit as st
import requests

st.set_page_config(
    page_title="Today's Environment",
    page_icon="👋",
)

if st.button("Rephrase Data"):
    with st.spinner("Contacting AI…"):
        try:
            data_response = requests.get("http://api:5000/latest-data")
            if data_response.status_code == 200:
                latest_data = data_response.json()
                res = requests.post(
                    "http://api:5000/environment", json=latest_data
                )
                ai_text = res.json().get("text", "No response.")
            else:
                ai_text = "No data."
        except requests.exceptions.RequestException as e:
            ai_text = f"An error occurred: {e}"
    st.write("**AI Says:**", ai_text)
