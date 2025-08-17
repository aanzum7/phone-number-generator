# ui.py
import streamlit as st
from config import THEMES

# Store current theme globally
CURRENT_THEME = {}

def apply_full_theme(operator: str):
    """Apply full screen theme based on selected operator."""
    global CURRENT_THEME
    theme = THEMES.get(operator)
    if not theme:
        return
    CURRENT_THEME = theme

    st.markdown(f"""
        <style>
        /* Full background */
        .stApp {{
            background-color: {theme['background']};
            color: {theme['text']};
        }}

        /* Headers */
        h1, h2, h3, h4, h5, h6 {{
            color: {theme['header']};
            text-align: center;
        }}

        /* Buttons (Generate & Download) */
        .stButton>button,
        div[data-testid="stDownloadButton"] > button {{
            background-color: {theme['button']} !important;
            color: white !important;
            border-radius: 8px;
            border: none;
            padding: 10px 18px;
            font-size: 16px;
            font-weight: bold;
            width: 100% !important;
            min-width: 100% !important;
            box-sizing: border-box;
            transition: all 0.3s ease;
        }}
        .stButton>button:hover,
        div[data-testid="stDownloadButton"] > button:hover {{
            background-color: {theme['button_hover']} !important;
            box-shadow: 0px 3px 12px rgba(0,0,0,0.2);
            transform: translateY(-1px);
        }}

        /* Cards / Containers */
        .stFrame {{
            background-color: {theme['card_bg']} !important;
            border-radius: 10px;
            padding: 10px;
        }}

        /* Inputs */
        input, .stNumberInput>div>div>input {{
            background-color: {theme['input_bg']};
            color: {theme['text']};
            border-radius: 6px;
            padding: 5px;
            width: 100%;
        }}

        /* Dataframe / Table */
        .stDataFrame thead th {{
            background-color: {theme['table_header']} !important;
            color: {theme['text']};
            text-align: center;
        }}
        .stDataFrame tbody td {{
            text-align: center;
        }}
        .stDataFrame tbody tr:nth-child(odd) {{
            background-color: {theme['table_row1']} !important;
        }}
        .stDataFrame tbody tr:nth-child(even) {{
            background-color: {theme['table_row2']} !important;
        }}
        </style>
    """, unsafe_allow_html=True)


def sidebar_info():
    """Sidebar with project info and author."""
    with st.sidebar:
        st.title("📌 About This Project")
        st.caption("""
            Generate **Bangladesh mobile numbers** quickly and easily.
            Select operator, prefix, count, and download in `xlsx` or `csv`.
        """)

        st.title("👨‍💻 Author: Tanvir Anzum")
        st.caption("""
            AI & Data Researcher | ML/NLP | Data & Growth Strategist
                      
            Passionate about creating **intelligent tools** and datasets.
        """)

        st.markdown("""
            🔗[LinkedIn](https://www.linkedin.com/in/aanzum) | 🔗[GitHub](https://github.com/aanzum7)
        """)


def get_theme_color():
    """Return main button/header color for preview or custom use."""
    return CURRENT_THEME.get('button', '#4CAF50')
