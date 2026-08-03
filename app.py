from utils.finpro_parser import FinproParser
import streamlit as st

st.set_page_config(
    page_title="AI-Based Sales & Demand Forecasting",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI-Based Sales & Demand Forecasting")
st.write("Upload your FINPRO Sales Bill Register.")

uploaded_file = st.file_uploader(
    "Choose an Excel File",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:

    parser = FinproParser(uploaded_file)

    clean_df = parser.extract_transactions()

    parser.save_csv(clean_df)

    st.success("Clean data saved to processed_data/clean_sales.csv")

    st.success("✅ File uploaded successfully!")

    st.subheader("Extracted Transactions")

    st.metric("Transactions", len(clean_df))
    st.dataframe(clean_df, use_container_width=True)
    products = sorted(clean_df["Product"].dropna().unique())

    st.metric("Products", len(products))
    st.subheader("Products Found")
    st.write(products)

else:
    st.info("Upload a FINPRO Sales Bill Register.")