# extract.py
import pandas as pd

def extract_data():
    print("Extracting data...")
    df = pd.read_csv("data_raw/sales_raw.csv")
    return df