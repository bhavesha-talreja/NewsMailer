import requests

import send_email

API_KEY = "9b820b3d72d74cfe907017d6b572d6d2"
url = (f"https://newsapi.org/v2/everything?"
       f"q=tesla&sortBy=publishedAt&apiKey={API_KEY}&language=en")

request = requests.get(url)
content = request.json()

lines = []

for item in content["articles"][:20]:
    title = item.get("title") or ""
    if title is not None:
        description = item.get("description") or ""
        url = item.get("url")
        lines.append(f"{title}\n{description}\n{url}")

emailbody = "\n\n".join(lines)

emailbody = f"Subject: Today's News\n\n{emailbody}"


emailbody = emailbody.encode('utf-8')
send_email.send_email(emailbody)