from utils.finpro_parser import FinproParser
import streamlit as st
import pandas as pd

# ------------------------
# Page Configuration
# ------------------------
st.set_page_config(
    page_title="AI-Based Sales & Demand Forecasting",
    page_icon="📈",
    layout="wide"
)

# ------------------------
# Title
# ------------------------
st.title("📈 AI-Based Sales & Demand Forecasting")

st.write("Upload your FINPRO Sales Bill Register to begin.")

# ------------------------
# File Upload
# ------------------------
uploaded_file = st.file_uploader(
    "Choose an Excel File",
    type=["xlsx", "xls"]
)

# ------------------------
# Read Excel
# ------------------------
if uploaded_file is not None:

    try:
        # Read exactly as it appears in Excel
        parser = FinproParser(uploaded_file)
        df = parser.read_excel()
        parser.inspect()

        st.success("✅ File uploaded successfully!")

        st.subheader("Preview of Raw FINPRO Report")

        st.write(df.head(20))

        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

    except Exception as e:

        st.error("Error reading the Excel file.")

        st.exception(e)

else:

    st.info("Please upload a FINPRO Excel report.")
