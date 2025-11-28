# transform.py
import pandas as pd

def transform_data(df):
    print("Transforming data...")

    # Fix date
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Replace missing customer names
    df["customer_name"]=df["customer_name"].fillna("UNKNOWN")

    # Replace missing values
    df["quantity"] = df["quantity"].fillna(1)
    df["price"] = df["price"].fillna(0)

    #fix product name
     # Replace missing customer names
    df["product_name"]=df["product_name"].fillna("UNKNOWN")

    # Convert types
    df["quantity"] = df["quantity"].astype(int)
    df["price"] = df["price"].astype(float)

    # Add new calculated column
    df["total_amount"] = df["quantity"] * df["price"]

    # Drop invalid rows
    df = df.dropna(subset=["order_date"])

    # Save clean file
    df.to_csv("data_clean/sales_clean.csv", index=False)

    return df
