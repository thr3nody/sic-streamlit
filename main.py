import streamlit as st
import requests

st.set_page_config(
    page_title="Today's Environment",
    page_icon="👋",
)

latest_data = {"CO": 0.4, "NO2": 0.03, "O3": 0.02}

if st.button("Rephrase Data"):
    with st.spinner("Contacting AI…"):
        res = requests.post("http://api:5000/environment", json=latest_data)
        ai_text = res.json().get("text", "No response.")
    st.write("**AI Says:**", ai_text)
