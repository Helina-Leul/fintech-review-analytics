import pandas as pd
from transformers import pipeline

print("Loading model...")

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

df = pd.read_csv(
    "data/raw/google_play_reviews_clean.csv"
)

results = []

for i, review in enumerate(df["review"]):

    try:

        prediction = classifier(
            str(review)[:512]
        )[0]

        results.append(
            {
                "review_id": i + 1,
                "review_text": review,
                "sentiment_label": prediction["label"],
                "sentiment_score": prediction["score"]
            }
        )

    except Exception:

        results.append(
            {
                "review_id": i + 1,
                "review_text": review,
                "sentiment_label": "NEUTRAL",
                "sentiment_score": 0.0
            }
        )

    if (i + 1) % 50 == 0:
        print(f"Processed {i+1} reviews")


output = pd.DataFrame(results)

output.to_csv(
    "data/raw/reviews_with_sentiment.csv",
    index=False
)

print("Sentiment analysis completed.")
