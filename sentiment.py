"""
Step 3: Sentiment Analysis on Reviews

"""

import pandas as pd
from textblob import TextBlob

raw = pd.read_csv("C:\\Users\\anish\\OneDrive\\Documents\\Desktop\\jupyter notbook\\DASHBOARD PROj\\amazon.csv")
clean = pd.read_csv("C:\\Users\\anish\\OneDrive\\Documents\\Desktop\\jupyter notbook\\DASHBOARD PROj\\amazon_cleaned.csv")

def get_sentiment(text):
    if pd.isna(text) or str(text).strip() == "":
        return None
    polarity = TextBlob(str(text)).sentiment.polarity  
    return polarity

raw["sentiment_score"] = raw["review_content"].apply(get_sentiment)

def label(score):
    if score is None:
        return "Unknown"
    if score > 0.1:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    return "Neutral"

raw["sentiment_label"] = raw["sentiment_score"].apply(label)

sentiment_df = raw[["product_id", "sentiment_score", "sentiment_label"]]
merged = clean.merge(sentiment_df, on="product_id", how="left")
merged = merged.drop_duplicates(subset="product_id")

merged.to_csv("amazon_with_sentiment.csv", index=False)

print("Sentiment label counts:")
print(merged["sentiment_label"].value_counts())

print("\nDoes text sentiment agree with star rating? (avg rating per sentiment label)")
print(merged.groupby("sentiment_label")["rating"].mean().round(2))

print("\nCategories with the most negative-sentiment products:")
neg = merged[merged["sentiment_label"] == "Negative"]
print(neg["main_category"].value_counts().head(5))