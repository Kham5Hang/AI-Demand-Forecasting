print("Forecast.py version 2 loaded")
print("Loaded:", __file__)
from prophet import Prophet
import pandas as pd


class SalesForecaster:

    def __init__(self, df):
        self.df = df

    def prepare_data(self, product, metric="Quantity"):

        data = self.df[self.df["Product"] == product]

        data = (
            data.groupby("Date")[metric]
            .sum()
            .reset_index()
        )
        

        data.columns = ["ds", "y"]
        data["ds"] = pd.to_datetime(data["ds"])

        return data

    def forecast(self, product, metric="Quantity", periods=30):

        data = self.prepare_data(product, metric)

        model = Prophet()

        model.fit(data)

        future = model.make_future_dataframe(periods=periods)

        return model.predict(future)

    