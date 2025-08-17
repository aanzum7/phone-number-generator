# app.py
import streamlit as st
from ui import apply_full_theme, sidebar_info, get_theme_color
from config import PREFIXES
from generator import generate_numbers
from exporter import export_data

# ---------------------------
# Sidebar
# ---------------------------
sidebar_info()

# ---------------------------
# Operator Selection
# ---------------------------
operator = st.selectbox("Choose Operator:", list(PREFIXES.keys()), index=0)
apply_full_theme(operator)  # Apply operator-specific full theme

# Prefix selection
prefix = PREFIXES[operator][0] if len(PREFIXES[operator]) == 1 else st.selectbox(
    "Choose Prefix:", PREFIXES[operator]
)

# Number of phone numbers to generate
count = st.number_input(
    "Number of numbers:",
    min_value=100,
    max_value=5000,
    value=3000,
    step=100
)

# Output format selection
file_format = st.radio(
    "Output Format:",
    ["xlsx", "csv"],
    index=0,
    horizontal=True
)

st.divider()

# ---------------------------
# Generate Numbers
# ---------------------------
generate_clicked = st.button("Generate Numbers", key="generate_fullwidth")

if generate_clicked:
    with st.spinner("Generating numbers..."):
        numbers = generate_numbers(operator, prefix, count)

    # Preview title with operator theme color
    theme_color = get_theme_color()
    st.markdown(f"""
        <h3 style='text-align:center; color:{theme_color}; margin-top:20px;'>
        Preview of Generated {operator} Numbers
        </h3>
    """, unsafe_allow_html=True)

    # Display table preview
    st.dataframe(numbers.head(10), use_container_width=True)

    # Export & Download button (fully themed)
    buffer, mime, filename = export_data(numbers, file_format)
    st.download_button(
        "📥 Download Generated Numbers",
        buffer,
        file_name=filename,
        mime=mime
    )

# Footer
st.markdown("""
    <p style='text-align:center; margin-top:30px; font-size:12px; color:#555;'>
    Demo available at: <a href='https://bdnumbergen.streamlit.app/' target='_blank'>
    https://bdnumbergen.streamlit.app/</a>
    </p>
""", unsafe_allow_html=True)
