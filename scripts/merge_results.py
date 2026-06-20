import pandas as pd


reviews = pd.read_csv(
    "data/raw/google_play_reviews_clean.csv"
)


analysis = pd.read_csv(
    "data/raw/final_analysis.csv"
)


final = pd.concat(
    [
        reviews.reset_index(drop=True),
        analysis[
            [
                "sentiment_label",
                "sentiment_score",
                "identified_theme"
            ]
        ]
    ],
    axis=1
)


final.to_csv(
    "data/raw/complete_reviews_analysis.csv",
    index=False
)


print(final.head())

print("\nColumns:")
print(final.columns)

print("\nShape:")
print(final.shape)

print("\nSaved complete_reviews_analysis.csv")
