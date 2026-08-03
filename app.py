from utils.finpro_parser import FinproParser
import streamlit as st
from models.forecast import SalesForecaster
import matplotlib.pyplot as plt

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
    selected_product = st.selectbox(
        "Select Product",
        products
    )

    days = st.slider(
        "Forecast Days",
        7,
        90,
        30
    )


    product_data = clean_df[clean_df["Product"] == selected_product]

    history = product_data["Date"].nunique()

    if history < 10:
        st.warning("Not enough historical data for forecasting.")

    elif st.button("Generate Forecast"):

        try:

            forecaster = SalesForecaster(clean_df)

            forecast = forecaster.forecast(selected_product, days)

            fig, ax = plt.subplots(figsize=(10, 5))

            history_df = forecaster.prepare_data(selected_product)

            ax.plot(
            history_df["ds"],
            history_df["y"],
            label="Historical Sales"
            )

            ax.plot(
                forecast["ds"],
                forecast["yhat"],
                label="Forecast"
            )

            ax.fill_between(
                forecast["ds"],
                forecast["yhat_lower"],
                forecast["yhat_upper"],
                alpha=0.2,
                label="Confidence Interval"
            )

            ax.set_title(selected_product)
            ax.legend()

            st.pyplot(fig)

            st.dataframe(
                forecast[["ds", "yhat"]].tail(days),
                use_container_width=True
            )

        except Exception as e:

            st.error(e)

else:
    st.info("Upload a FINPRO Sales Bill Register.")