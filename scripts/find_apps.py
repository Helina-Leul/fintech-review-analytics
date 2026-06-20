from google_play_scraper import search


apps = search(
    "Dashen Bank Mobile Banking",
    lang="en",
    country="et"
)


for app in apps[:10]:
    print(
        app["title"],
        app["appId"]
    )
