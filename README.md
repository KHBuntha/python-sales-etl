# From this one project, you demonstrated:
✅ Python ETL design
✅ Data cleansing & transformation
✅ SQL Server loading
✅ Config-driven connection
✅ Debugging drivers & authentication
✅ Professional file structure
✅ GitHub-ready project
✅ Production-safe pandas logic

# Python Sales ETL Project

## Overview
This project demonstrates a complete ETL process using Python and SQL Server.

### Workflow
1. Extract CSV data
2. Transform: clean, validate, enrich
3. Load into SQL Server fact_sales table

### Tech Stack
- Python
- Pandas
- SQL Server
- pyodbc

## Output
Data loaded into table: fact_sales

## Sample Transformation
- Invalid dates removed
- NULL values cleaned
- Total amount calculation

## How to Run
1. Update config.json
2. Run:
   python main.py

## Installation and fixing by cases:
- You can verify phyton works with show version value by run cmd: python --version
- 'python' is not recognized so you need to install phyton first
- invalid command pip: because you did install Phyton, so you need to download and install Phyton by download from Phyton official site. don't donload from Microsoft store because some configuration or version not compatible
- python -m pip --version
- when install pip recommend check Add "Python to PATH" automatically
- if you did not check so you need to manually
    1. Check correct path of phyton by cmd "where python"
    2. Copy that directory these two paths: 
    C:\Users\YourName\AppData\Local\Programs\Python\Python39\
    C:\Users\YourName\AppData\Local\Programs\Python\Python39\Scripts\
    add these bot to path:
    System Properties → Environment Variables → Path
- DISABLE MICROSOFT STORE ALIAS (IMPORTANT)
Settings → Apps → Apps & features → Advanced app settings → execution aliases
Turn OFF:
python.exe
python3.exe

- Install drive for odbc connection from phyton to sql server: 
open and run cmd command: pip install pyodbc pandas
- Create Databsae name in sql server:
Open sql server management and then run script: CREATE DATABASE SalesDW;
- Run issue:
pyodbc.InterfaceError: ('28000', "[28000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Login failed for user 'usertest'. (18456) (SQLDriverConnect); [28000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Login failed for user 'usertest'. (18456)")
THIS IS ISSUE CAN BE FROM YOUR SQL AUTHENTICATION (user,password,etc.) PROBLEM AND PHYTHON IMPORTING FILE HAVEN'T CORRECT.
-Import file issue: FIX PYTHON PATH IN VS CODE / PYCHARM
Ctrl + Shift + P
Python: Select Interpreter
Restart VS Code.
