"""
Step 1: Data Cleaning
Reads the raw Kaggle-style Amazon dataset and produces a clean CSV
ready for SQL loading and analysis.
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\anish\\OneDrive\\Documents\\Desktop\\jupyter notbook\\DASHBOARD PROj\\amazon.csv")
print("Raw shape:", df.shape)

df["discounted_price"] = (
    df["discounted_price"].astype(str).str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False).astype(float)
)
df["actual_price"] = (
    df["actual_price"].astype(str).str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False).astype(float)
)

df["discount_percentage"] = (
    df["discount_percentage"].astype(str).str.replace("%", "", regex=False).astype(float)
)

df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df["rating_count"] = (
    df["rating_count"].astype(str).str.replace(",", "", regex=False)
)
df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce")

df["main_category"] = df["category"].astype(str).str.split("|").str[0]
df["sub_category"] = df["category"].astype(str).str.split("|").str[-1]

before = len(df)
df = df.dropna(subset=["discounted_price", "actual_price", "rating", "rating_count"])
print(f"Dropped {before - len(df)} rows with missing price/rating data")

before = len(df)
df = df.drop_duplicates(subset=["product_id"])
print(f"Dropped {before - len(df)} duplicate product_id rows")

df["savings_amount"] = df["actual_price"] - df["discounted_price"]
df["price_bucket"] = pd.cut(
    df["discounted_price"],
    bins=[0, 500, 1500, 5000, 20000, np.inf],
    labels=["Under 500", "500-1500", "1500-5000", "5000-20000", "20000+"]
)

core_cols = [
    "product_id", "product_name", "main_category", "sub_category",
    "actual_price", "discounted_price", "discount_percentage",
    "savings_amount", "price_bucket", "rating", "rating_count"
]
df_core = df[core_cols].copy()

df_core.to_csv("amazon_cleaned.csv", index=False)
print("Cleaned shape:", df_core.shape)
print(df_core.head())