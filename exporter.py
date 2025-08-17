# exporter.py
import pandas as pd
from io import BytesIO
import streamlit as st

def export_data(numbers: list[str], file_format: str = "xlsx") -> BytesIO:
    """
    Export numbers as CSV or Excel and return BytesIO for Streamlit download.
    """
    df = pd.DataFrame(numbers, columns=["Mobile_Number"])
    buffer = BytesIO()

    if file_format.lower() == "xlsx":
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Numbers")
        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        filename = "BD_Mobile_Numbers.xlsx"
    else:
        df.to_csv(buffer, index=False)
        mime = "text/csv"
        filename = "BD_Mobile_Numbers.csv"

    buffer.seek(0)
    return buffer, mime, filename
