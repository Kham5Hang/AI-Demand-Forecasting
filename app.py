from utils.finpro_parser import FinproParser
import streamlit as st

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

    parser = FinproParser(uploaded_file)

    df = parser.read_excel()

    rows, cols = parser.get_sheet_size()

    st.success("✅ File uploaded successfully!")

    col1, col2 = st.columns(2)

    col1.metric("Rows", rows)
    col2.metric("Columns", cols)

    st.subheader("Raw Data Preview")
    clean_df = parser.extract_transactions()
    st.dataframe(clean_df, use_container_width=True)

    header_row = parser.find_header_row()

    if header_row is not None:
        st.success(f"Header row found at row {header_row}")
    else:
        st.error("Header row not found.")

else:
    st.info("Upload a FINPRO Sales Bill Register.")