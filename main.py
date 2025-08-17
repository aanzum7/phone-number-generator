# app.py
import streamlit as st
from config import PREFIXES
from ui import select_prefix, apply_theme, sidebar_info
from generator import generate_numbers
from exporter import export_data

# ---------------------------
# 🌐 Streamlit Page Config
# ---------------------------
st.set_page_config(page_title="BD Mobile Number Generator", layout="wide")

# ---------------------------
# Sidebar Info
# ---------------------------
sidebar_info()

# ---------------------------
# Main Header
# ---------------------------
st.markdown("<h1 style='text-align:center;'>📱 Bangladesh Mobile Number Generator</h1>", unsafe_allow_html=True)

# ---------------------------
# Operator Selection
# ---------------------------
operator = st.selectbox("Choose Operator", options=list(PREFIXES.keys()), format_func=lambda x: x.capitalize())

# Apply operator theme dynamically
apply_theme(operator)

# ---------------------------
# Prefix Selection
# ---------------------------
prefix = select_prefix(operator)

# ---------------------------
# Number Count Input
# ---------------------------
count = st.slider("How many numbers to generate?", min_value=100, max_value=5000, value=3000, step=100)

# ---------------------------
# File Format Selection
# ---------------------------
file_format = st.radio("Select Output Format", options=["xlsx", "csv"], index=0)

# ---------------------------
# Generate Button
# ---------------------------
if st.button("Generate Numbers 🚀"):
    if not prefix:
        st.error("Prefix not selected. Cannot generate numbers.")
    else:
        numbers = generate_numbers(operator, prefix, count)
        st.success(f"✅ Generated {len(numbers)} numbers for {operator.capitalize()}!")

        # Preview first 10 numbers
        st.dataframe(numbers[:10], width=400)

        # Export and download
        buffer, mime, filename = export_data(numbers, file_format)
        st.download_button(
            label=f"📥 Download {file_format.upper()} File",
            data=buffer,
            file_name=filename,
            mime=mime,
            use_container_width=True
        )
