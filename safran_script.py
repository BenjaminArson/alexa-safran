import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

url = "https://www.boursorama.com/cours/actualites/SAF"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select("a.c-media")[:5]

flash_briefing = []

for i, article in enumerate(articles):
    title = article.select_one(".c-media__title").get_text(strip=True)
    link = "https://www.boursorama.com" + article.get("href")
    
    item = {
        "uid": f"safran-{i}",
        "updateDate": datetime.utcnow().isoformat() + "Z",
        "titleText": "Actualité SAFRAN",
        "mainText": title,
        "redirectionUrl": link
    }
    flash_briefing.append(item)

with open("flashbriefing.json", "w", encoding="utf-8") as f:
    json.dump(flash_briefing, f, ensure_ascii=False, indent=2)
