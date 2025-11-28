# main.py
from extract import extract_data
from transform import transform_data
from load import load_to_sql

def run_pipeline():
    df = extract_data()
    clean_df = transform_data(df)
    load_to_sql(clean_df)
    

if __name__ == "__main__":
    run_pipeline()
