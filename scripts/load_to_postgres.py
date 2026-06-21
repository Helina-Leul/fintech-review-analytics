import pandas as pd
import psycopg2

# Load dataset
df = pd.read_csv(
    "data/raw/complete_reviews_analysis.csv"
)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="Leul78Amete"
)

cur = conn.cursor()

# Insert banks first
banks = [
    ("Commercial Bank of Ethiopia", "CBE Mobile Banking"),
    ("Bank of Abyssinia", "BOA Mobile Banking"),
    ("Dashen Bank", "Dashen Mobile")
]

for bank in banks:
    cur.execute(
        """
        INSERT INTO banks (bank_name, app_name)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING
        """,
        bank
    )

conn.commit()

# Get bank ids
cur.execute("SELECT bank_id, bank_name FROM banks")
bank_map = dict(cur.fetchall())

# Insert reviews
for _, row in df.iterrows():

    bank_name = row["bank"]

    bank_id = None

    for bid, bname in bank_map.items():
        if bname == bank_name:
            bank_id = bid

    cur.execute(
        """
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            identified_theme,
            source
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            bank_id,
            row["review"],
            int(row["rating"]),
            row["date"],
            row["sentiment_label"],
            float(row["sentiment_score"]),
            row["identified_theme"],
            row["source"]
        )
    )

conn.commit()

print("Reviews inserted successfully.")

cur.close()
conn.close()
