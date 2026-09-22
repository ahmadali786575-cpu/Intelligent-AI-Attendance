
import streamlit as st

def footer_home():
    logo_url = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='110' height='65' viewBox='0 0 90 55'%3E%3Ctext x='45' y='23' text-anchor='middle' font-family='Arial,sans-serif' font-size='24' font-weight='700' fill='%23333333'%3EAHMAD%3C/text%3E%3Ctext x='45' y='48' text-anchor='middle' font-family='Arial,sans-serif' font-size='24' font-weight='700' fill='%23FFC107'%3EALI%3C/text%3E%3C/svg%3E"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight:bold; color:white" >Created with ❤️ by </p>
            <img src="{logo_url}" style="max-height:25px">
        </div>

        """, unsafe_allow_html=True
    )


def footer_dashboard():
    logo_url = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='110' height='65' viewBox='0 0 90 55'%3E%3Ctext x='45' y='23' text-anchor='middle' font-family='Arial,sans-serif' font-size='24' font-weight='700' fill='%23333333'%3EAHMAD%3C/text%3E%3Ctext x='45' y='48' text-anchor='middle' font-family='Arial,sans-serif' font-size='24' font-weight='700' fill='%23FFC107'%3EALI%3C/text%3E%3C/svg%3E"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight:bold; color:black" >Created with ❤️ by </p>
            <img src="{logo_url}" style="max-height:25px">
        </div>

        """, unsafe_allow_html=True
    )