Title

Customer Experience Analytics for Ethiopian Fintech Apps

1. Executive Summary

Explain:

analyzed Google Play reviews
CBE, BOA, Dashen
NLP sentiment analysis
theme extraction
PostgreSQL storage
business recommendations
2. Data Collection

Include:

Your numbers:

Total reviews: 805

Dashen Bank: 395
Commercial Bank of Ethiopia: 273
Bank of Abyssinia: 137

Mention limitation:

Google Play scraping returned fewer than the requested 400 reviews for some apps due to availability and scraping limits.

3. Data Quality

Use your results:

Duplicates removed
Missing values: 0
Final dataset: 805 reviews
4. Sentiment Analysis

Include:

Model:

distilbert-base-uncased-finetuned-sst-2-english

Results:

Positive: 434
Negative: 371

Explain:

Positive reviews indicate satisfaction.
Negative reviews reveal product issues.

5. Theme Analysis

Your themes:

Other
Positive Experience
Account Access Issues
Transaction Performance
UI & Experience
App Performance
Feature Requests
Complaints
OTP Problems
6. Database Design

Show:

Tables:

banks

bank_id
bank_name
app_name


reviews

review_id
bank_id
review_text
rating
sentiment
theme

Mention PostgreSQL.

7. Visualizations

Insert your 3 images:

From:

reports/plots/

Add:

sentiment_by_bank.png
rating_by_bank.png
top_themes.png
8. Insights

Based on your data:

Commercial Bank of Ethiopia

Drivers:

Positive experience
Good accessibility

Pain points:

Login problems
OTP issues

Recommendations:

Improve authentication reliability
Reduce login failures
Dashen Bank

Drivers:

Highest average rating

Your result:

3.98

Pain points:

Transaction issues
App performance

Recommendations:

Optimize transaction speed
Improve stability
Bank of Abyssinia

Average:

3.53

Pain points:

Account access
Performance issues

Recommendations:

Improve app reliability
Improve support response
9. Ethical Considerations

Mention:

Review bias
Angry users more likely to post
Google Play users are not all customers
Data does not represent all Ethiopian banking users
10. Conclusion

Summarize:

The analysis converts user feedback into actionable product improvements.
