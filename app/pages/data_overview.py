"""app/pages/data_overview.py"""

import streamlit as st
import os
from app.utils.data_loader import load_uci_data

def app():
    st.title("📊 Data Overview – UCI Credit Default")

    df, status_msg = load_uci_data()
    st.success(status_msg)

    st.write("### Preview of Dataset")
    st.dataframe(df.head())

    st.write("### Class Distribution")
    st.bar_chart(df["default"].value_counts())

    # Save to disk
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df.to_csv(os.path.join(output_dir, "cleaned_sample.csv"), index=False)

    # Let user download it too
    st.download_button(
        label="Download Cleaned CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="cleaned_credit_data.csv",
        mime="text/csv"
    )

