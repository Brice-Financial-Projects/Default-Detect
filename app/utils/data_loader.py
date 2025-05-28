
"""app/utils/data_loader.py"""
import pandas as pd

@st.cache_data
def load_data(path):
    return pd.read_csv(path)
