import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def fetch_data_from_sql():
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost,1433;"
        "DATABASE=MarketingAnalytics;"
        "UID=sa;"
        "PWD=Himanshu@1234;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    conn = pyodbc.connect(conn_str)

    query = """
SELECT 
    cr.ReviewID,
    cr.CustomerID,
    c.CustomerName,
    g.Country,
    cr.ProductID,
    p.ProductName,
    cr.Rating,
    cr.ReviewText,
    cr.ReviewDate
FROM customer_reviews cr
LEFT JOIN customers c ON cr.CustomerID = c.CustomerID
LEFT JOIN geography g ON c.GeographyID = g.GeographyID
LEFT JOIN products p ON cr.ProductID = p.ProductID
"""

    df = pd.read_sql(query, conn)
    conn.close()
    return df

customer_reviews_df = fetch_data_from_sql()

sia = SentimentIntensityAnalyzer()

def calculate_sentiment(review):
    sentiment = sia.polarity_scores(str(review))
    return sentiment["compound"]

def categorize_sentiment(score, rating):
    if score > 0.05:
        if rating >= 4:
            return "Positive"
        elif rating == 3:
            return "Mixed Positive"
        else:
            return "Mixed Negative"
    elif score < -0.05:
        if rating <= 2:
            return "Negative"
        elif rating == 3:
            return "Mixed Negative"
        else:
            return "Mixed Positive"
    else:
        if rating >= 4:
            return "Positive"
        elif rating <= 2:
            return "Negative"
        else:
            return "Neutral"

def sentiment_bucket(score):
    if score >= 0.5:
        return "0.5 to 1.0"
    elif 0.0 <= score < 0.5:
        return "0.0 to 0.49"
    elif -0.5 <= score < 0.0:
        return "-0.49 to 0.0"
    else:
        return "-1.0 to -0.5"

customer_reviews_df["SentimentScore"] = customer_reviews_df["ReviewText"].apply(calculate_sentiment)

customer_reviews_df["SentimentCategory"] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row["SentimentScore"], row["Rating"]),
    axis=1
)

customer_reviews_df["SentimentBucket"] = customer_reviews_df["SentimentScore"].apply(sentiment_bucket)

print(customer_reviews_df.head())

customer_reviews_df.to_csv(
    "/Users/himanshujain/Desktop/Project/customer_reviews_with_sentiment.csv",
    index=False
)
