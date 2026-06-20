import pandas as pd


df = pd.read_csv(
    "data/raw/reviews_with_sentiment.csv"
)


def assign_theme(text):

    text = str(text).lower()

    if any(word in text for word in [
        "login",
        "log in",
        "sign in",
        "password",
        "account",
        "access"
    ]):
        return "Account Access Issues"


    elif any(word in text for word in [
        "otp",
        "verification",
        "code",
        "sms"
    ]):
        return "OTP Problems"


    elif any(word in text for word in [
        "transfer",
        "transaction",
        "send",
        "payment",
        "money"
    ]):
        return "Transaction Performance"


    elif any(word in text for word in [
        "slow",
        "crash",
        "freeze",
        "hang",
        "loading",
        "error",
        "bug"
    ]):
        return "App Performance"


    elif any(word in text for word in [
        "design",
        "interface",
        "beautiful",
        "easy",
        "simple",
        "friendly",
        "ui"
    ]):
        return "UI & Experience"


    elif any(word in text for word in [
        "feature",
        "finger",
        "biometric",
        "update",
        "request"
    ]):
        return "Feature Requests"


    elif any(word in text for word in [
        "good",
        "great",
        "best",
        "excellent",
        "love",
        "amazing"
    ]):
        return "Positive Experience"


    elif any(word in text for word in [
        "bad",
        "worst",
        "problem",
        "issue",
        "fail"
    ]):
        return "Complaints"


    else:
        return "Other"



# apply theme detection
df["identified_theme"] = df["review_text"].apply(assign_theme)


# save output
df.to_csv(
    "data/raw/final_analysis.csv",
    index=False
)


print(
    df["identified_theme"].value_counts()
)


print("\nTheme extraction completed.")
