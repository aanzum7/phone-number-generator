# ui.py
import streamlit as st
from config import THEMES, PREFIXES

def select_prefix(operator: str) -> str:
    """
    Return the prefix for the selected operator.
    - If multiple prefixes exist, show a dropdown for user selection.
    - If only one prefix, auto-select it.
    """
    prefixes = PREFIXES.get(operator, [])
    if len(prefixes) > 1:
        return st.selectbox(f"Choose prefix for {operator}", prefixes)
    elif len(prefixes) == 1:
        st.markdown(f"**Prefix auto-selected:** {prefixes[0]}")
        return prefixes[0]
    else:
        return ""

def apply_theme(operator: str):
    """
    Apply operator theme colors dynamically to headers and buttons.
    """
    colors = THEMES.get(operator, {"primary": "#333333", "secondary": "#eeeeee"})
    st.markdown(
        f"""
        <style>
        h1 {{ color: {colors['primary']}; }}
        .stButton>button {{ background-color: {colors['primary']}; color: white; border-radius: 10px; }}
        .stButton>button:hover {{ filter: brightness(1.1); }}
        </style>
        """,
        unsafe_allow_html=True
    )

def sidebar_info():
    """Render sidebar with project and author info"""
    st.sidebar.title("📖 About Project")
    st.sidebar.info(
        """
        Generate random Bangladesh mobile numbers for:
        - Airtel, GP, Robi, Banglalink
        - Auto-prefix selection or choose from multiple
        - Export as CSV or Excel
        """
    )
    st.sidebar.markdown("---")
    st.sidebar.title("👨‍💻 About Author")
    st.sidebar.markdown(
        "**Tanvir Anzum**  \nAnalytics Scientist & Strategist  \nPassionate about Data & AI"
    )
