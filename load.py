# load.py
import pyodbc
import json

def load_to_sql(df):
    print("Loading into SQL Server...")

    config = json.load(open("config.json"))

    conn_str = f"""
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER={config['server']};
    DATABASE={config['database']};
    UID={config['username']};
    PWD={config['password']};
    """

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # cursor.execute(f"""
    # IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='fact_sales')
    # CREATE TABLE fact_sales (
    #     order_id INT,
    #     order_date DATE,
    #     customer_name VARCHAR(100),
    #     product VARCHAR(50),
    #     quantity INT,
    #     price FLOAT,
    #     total_amount FLOAT
    # )
    # """)
    # conn.commit()
        

    for index, row in df.iterrows():
        # print(row)
        #total_amount = int(row.quantity) * float(row.price)
        #print (row)

        cursor.execute("""
        INSERT INTO fact_sales (order_id, order_date, customer_name, product_name, quantity, price, total_amount)
        VALUES (?,?,?,?,?,?,?) """,
        int(row.order_id),
        row.order_date.to_pydatetime().date() if hasattr(row.order_date, "to_pydatetime") else row.order_date,
        str(row.customer_name),
        str(row.product_name).strip(),
        int(row.quantity),
        float(row.price),
        float(row.total_amount)
        )

    conn.commit()
    conn.close()
