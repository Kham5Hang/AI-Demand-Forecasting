import pandas as pd


class FinproParser:

    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file

    def read_excel(self):
        return pd.read_excel(self.uploaded_file, header=None)

    def get_sheet_size(self):
        df = self.read_excel()
        return df.shape

    def preview(self, rows=20):
        df = self.read_excel()
        return df.head(rows)
    