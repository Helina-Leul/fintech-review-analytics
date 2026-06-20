import pandas as pd

df = pd.read_csv("data/raw/google_play_reviews.csv")

before = len(df)

df = df.drop_duplicates(subset=["review"])
df = df.dropna(subset=["review", "rating"])

df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

after = len(df)

print(f"Rows before cleaning: {before}")
print(f"Rows after cleaning: {after}")

df.to_csv(
    "data/raw/google_play_reviews_clean.csv",
    index=False
)

print("Clean dataset saved.")
