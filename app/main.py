"""app/main.py"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st

import app.pages.home as home
import app.pages.problem_statement as problem_statement
import app.pages.data_overview as data_overview
import app.pages.model_development as model_development
import app.pages.results as results

st.set_page_config(page_title="Default Detect", layout="wide")

PAGES = {
    "Home": home,
    "Problem Statement": problem_statement,
    "Data Overview": data_overview,
    "Model Development": model_development,
    "Results": results,
}

selection = st.sidebar.radio("Select Page", list(PAGES.keys()))
PAGES[selection].app()

