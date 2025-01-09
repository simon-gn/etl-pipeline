import sys
import os
import pandas as pd
from etl.data_cleaning import clean_data
from etl.load_data import load_to_postgres
from .database import get_db_connection

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


def load_data():
    engine = get_db_connection()

    raw_data = pd.read_csv("../data/raw/Amazon Sale Report.csv")
    cleaned_data = clean_data(raw_data)
    cleaned_data.to_csv("../data/processed/cleaned_data.csv", index=False)

    load_to_postgres(cleaned_data, "sales_data", engine)
