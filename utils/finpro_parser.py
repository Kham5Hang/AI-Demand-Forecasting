import pandas as pd


class FinproParser:

    def __init__(self, uploaded_file):
        self.df = pd.read_excel(uploaded_file, header=None)

    def extract_transactions(self):

        records = []
        current_product = None

        for _, row in self.df.iterrows():

            # Product row
            if (
                pd.isna(row[0])
                and pd.notna(row[1])
                and isinstance(row[2], str)
                and "Customer" not in row[2]
            ):
                current_product = row[2]
                continue

            # Transaction row
            if pd.notna(row[0]) and current_product is not None:

                records.append({
                    "Date": row[0],
                    "Product": current_product,
                    "Document No": row[1],
                    "Customer": row[2],
                    "Quantity": row[5],
                    "Rate": row[6],
                    "Gross Amount": row[7],
                    "Discount": row[8],
                    "Net Amount": row[10]
                })

        return pd.DataFrame(records)