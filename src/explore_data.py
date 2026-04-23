import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "online_retail_II.csv"

### DATA EXPLORATION ###

def explore_data():
    print("Loading dataset...\n")

    df = pd.read_csv(DATA_PATH, encoding="ISO-8859-1")

    df.columns = df.columns.str.strip().str.replace(" ", "_")

    print("Dataset loaded.\n")

    print("*** SHAPE ***")
    print(df.shape)

    print("\n*** FIRST 5 ROWS ***")
    print(df.head())

    print("\n*** DATA INFO ***")
    print(df.info())

    print("\n *** MISSING VALUES ***")
    print(df.isna().sum())

    print("\n *** NEGATIVE QUANTITY ***")
    print((df["Quantity"] <= 0).sum())

    print("\n*** ZERO OR NEGATIVE PRICE ***")
    print((df["Price"] <= 0).sum())

    print("\n*** CANCELLED INVOICES ***")
    print(df["Invoice"].astype(str).str.startswith("C").sum())

    return df

if __name__ == "__main__":
    explore_data()