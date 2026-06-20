from google_play_scraper import reviews, Sort
import pandas as pd
import os


def scrape_bank(app_id, bank_name):

    print(f"Scraping {bank_name}")

    all_reviews = []

    continuation_token = None


    while True:

        result, continuation_token = reviews(
            app_id,
            lang="en",
            country="et",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token
        )


        all_reviews.extend(result)


        print(
            bank_name,
            "collected:",
            len(all_reviews)
        )


        if continuation_token is None:
            break


        if len(all_reviews) >= 500:
            break



    data=[]


    for r in all_reviews:

        data.append({

            "review": r["content"],
            "rating": r["score"],
            "date": r["at"].strftime("%Y-%m-%d"),
            "bank": bank_name,
            "source": "Google Play"

        })


    return pd.DataFrame(data)




def main():


    apps={


        "Commercial Bank of Ethiopia":
        "com.combanketh.ethiodirect",


        "Bank of Abyssinia":
        "africa.of.boamobile",


        "Dashen Bank":
        "com.cr2.amolelight"

    }



    dfs=[]


    for bank, app in apps.items():

        df=scrape_bank(
            app,
            bank
        )

        dfs.append(df)



    final=pd.concat(
        dfs,
        ignore_index=True
    )


    print("\nBefore cleaning")
    print(final.shape)



    final.drop_duplicates(
        subset=["review"],
        inplace=True
    )


    final.dropna(
        subset=["review","rating"],
        inplace=True
    )


    print("\nAfter cleaning")
    print(final.shape)



    os.makedirs(
        "data/raw",
        exist_ok=True
    )


    final.to_csv(
        "data/raw/google_play_reviews.csv",
        index=False
    )


    print("Saved successfully")



if __name__=="__main__":
    main()
