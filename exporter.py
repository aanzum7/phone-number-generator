# exporter.py
from io import BytesIO
import pandas as pd

def export_data(df, file_format="xlsx"):
    if file_format == "xlsx":
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Numbers")
        buffer.seek(0)
        return buffer, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "bd_mobile_numbers.xlsx"
    else:  # CSV
        buffer = BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        return buffer, "text/csv", "bd_mobile_numbers.csv"
