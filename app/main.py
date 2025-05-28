"""app/main.py"""

import streamlit as st
from app.pages import (
    Home,
    Problem_Statement,
    Data_Overview,
    Model_Development,
    Results,
)

st.set_page_config(page_title="Default Detect", layout="wide")

PAGES = {
    "Home": Home,
    "Problem Statement": Problem_Statement,
    "Data Overview": Data_Overview,
    "Model Development": Model_Development,
    "Results": Results,
}

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
