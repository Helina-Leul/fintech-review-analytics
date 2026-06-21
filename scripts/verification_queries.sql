-- Task 3 Database Verification Queries

-- 1. Count reviews per bank

SELECT
    b.bank_name,
    COUNT(*) AS total_reviews
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name;


-- 2. Average rating per bank

SELECT
    b.bank_name,
    ROUND(AVG(r.rating),2) AS avg_rating
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name;


-- 3. Check missing values

SELECT
    COUNT(*) FILTER (WHERE review_text IS NULL) AS missing_review,
    COUNT(*) FILTER (WHERE rating IS NULL) AS missing_rating,
    COUNT(*) FILTER (WHERE sentiment_label IS NULL) AS missing_sentiment
FROM reviews;


-- 4. Total number of reviews

SELECT COUNT(*) AS total_reviews
FROM reviews;
