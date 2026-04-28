import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "online_retail_II.csv"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "cleaned_data.csv"

def clean_data():
    print("Loading data...")

    df = pd.read_csv(DATA_PATH, encoding="ISO-8859-1")

    df.columns = df.columns.str.strip().str.replace(" ", "_")

    print("Initial shape:", df.shape)

    df = df.dropna(subset=["Customer_ID"])

    df = df[df["Quantity"] > 0]

    df = df[df["Price"] > 0]

    df = df[~df["Invoice"].astype(str).str.startswith("C")]

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    print("Cleaned shape:", df.shape)

    print("Rows removed:", 1067371 - 805549)

    df.to_csv(OUTPUT_PATH, index=False)

    return df

if __name__ == "__main__":
    clean_data()