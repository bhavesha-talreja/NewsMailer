import requests

API_KEY = "9b820b3d72d74cfe907017d6b572d6d2"
url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={API_KEY}"

request = requests.get(url)
content = request.json()

for item in content["articles"]:
    print(item["title"])
    print(item["description"])