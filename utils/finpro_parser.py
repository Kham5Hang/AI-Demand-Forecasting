import streamlit as st
import pandas as pd


class FinproParser:

    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file

    def read_excel(self):

        df = pd.read_excel(
            self.uploaded_file,
            header=None
        )

        return df

    def inspect(self):

        df = self.read_excel()

        st.subheader("First 25 Rows of the Raw Excel")

        st.dataframe(df.head(25), use_container_width=True)