import streamlit as st
from supabase import create_client, Client


if "SUPABASE_URL" not in st.secrets:
    st.error("SUPABASE_URL is missing from Streamlit Cloud Secrets.")
    st.stop()

if "SUPABASE_KEY" not in st.secrets:
    st.error("SUPABASE_KEY is missing from Streamlit Cloud Secrets.")
    st.stop()


supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)