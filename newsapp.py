import requests
import json

query = input("which news you want to see : ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-07-13&sortBy=publishedAt&apiKey=179e49a46e2542abaa34dce8e68824ea"
r = requests.get(url)
news = json.loads(r.text)
#print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------")
