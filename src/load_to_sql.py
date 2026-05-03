import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "cleaned_data.csv"
DB_PATH = BASE_DIR / "database" / "customer_revenue.db"


def load_data():
    print("Loading cleaned data...")

    df = pd.read_csv(DATA_PATH)

    conn = sqlite3.connect(DB_PATH)

    df.to_sql("transactions", conn, if_exists="replace", index=False)

    print("Data loaded into SQLite")

    conn.close()


if __name__ == "__main__":
    load_data()