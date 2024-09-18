# app.py
import streamlit as st

# Import your pages
from chat import chat_app
from pdfreader import pdf_reader_app

# Set up page configuration
st.set_page_config(page_title="Multi-Page App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Chat", "PDF Reader"])

# Display selected page
if page == "Chat":
    chat_app()  # This function runs the chat app
elif page == "PDF Reader":
    pdf_reader_app()  # This function runs the PDF reader app
