
"""app/utils/data_loader.py"""

import os
import pandas as pd
import streamlit as st


@st.cache_data
def load_uci_data():
    csv_path = "data/raw/uci_credit_data.csv"
    xls_path = "data/raw/uci_credit_data.xls"

    message = ""

    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        message = "📄 Loaded from CSV."
    elif os.path.exists(xls_path):
        df = pd.read_excel(xls_path, header=1)
        df.to_csv(csv_path, index=False)
        message = "🧾 Loaded from XLS and converted to CSV."
    else:
        st.error("❌ Dataset not found in `data/raw/`.")
        st.stop()

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df.rename(columns={"default_payment_next_month": "default"}, inplace=True)

    return df, message



