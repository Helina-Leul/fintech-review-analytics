import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv(
    "data/raw/complete_reviews_analysis.csv"
)

os.makedirs("reports/plots", exist_ok=True)


# 1. Sentiment distribution by bank

sentiment = (
    df.groupby(["bank","sentiment_label"])
    .size()
    .unstack()
)

sentiment.plot(
    kind="bar",
    figsize=(10,6)
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig(
    "reports/plots/sentiment_by_bank.png"
)

plt.close()


# 2. Average rating by bank

rating = (
    df.groupby("bank")["rating"]
    .mean()
)

rating.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Average Rating by Bank")
plt.ylabel("Rating")

plt.tight_layout()

plt.savefig(
    "reports/plots/rating_by_bank.png"
)

plt.close()


# 3. Themes

themes = (
    df["identified_theme"]
    .value_counts()
    .head(10)
)

themes.plot(
    kind="barh",
    figsize=(8,6)
)

plt.title("Top Review Themes")

plt.tight_layout()

plt.savefig(
    "reports/plots/top_themes.png"
)

plt.close()


print("Plots created successfully")
