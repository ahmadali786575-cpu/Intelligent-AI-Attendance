
import streamlit as st

def footer_home():

    logo_url = logo_url = logo_url = "https://placehold.co/100x45/5865F2/111111.svg?text=AHMAD%0AALI"
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p>Created with ❤️ by </p>
            <img src="{logo_url}" style="max-height:25px">
        </div>

        """, unsafe_allow_html=True
    )