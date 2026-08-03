import pandas as pd


class FinproParser:

    def __init__(self, uploaded_file):
        self.df = pd.read_excel(uploaded_file, header=None)
    

    def is_product_row(self, row):

        return (
            pd.isna(row[0])
            and pd.notna(row[1])
            and isinstance(row[2], str)
            and row[2].strip() != ""
        )

    def is_transaction_row(self, row):
        return pd.notna(row[0])

    def extract_transactions(self):

        current_product = None
        records = []

        for _, row in self.df.iterrows():

            if self.is_product_row(row):
                current_product = row[2]
                continue

            if self.is_transaction_row(row) and current_product:

                records.append({
                    "Date": row[0],
                    "Product": current_product,
                    "Document No": row[1],
                    "Customer": row[2],
                    "UoM": row[4],
                    "Quantity": row[5],
                    "Rate": row[6],
                    "Gross Amount": row[7],
                    "Discount": row[8],
                    "Net Amount": row[10]
                })

        clean_df = pd.DataFrame(records)

        clean_df = clean_df[
            ~clean_df["Date"].astype(str).str.contains(
                "Generated|Printed|Export",
                case=False,
                na=False
            )
        ]

        return clean_df


    def save_csv(self, df, filename="processed_data/clean_sales.csv"):
        df.to_csv(filename, index=False)