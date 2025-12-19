import requests
from bs4 import BeautifulSoup
import csv
import datetime
import os
url = "https://finance.yahoo.com/quote/%5EGSPC"
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "html.parser")
price_el = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
if not price_el:
    raise RuntimeError("Could not locate price element on the page.")
price = price_el.text.strip()
print("=" * 60)
print("S&P 500 PRICE TRACKER")
print("=" * 60)
print(f"Current S&P 500 Price: {price}")
print()
csv_file = "sp500_price_data.csv"
file_exists = os.path.isfile(csv_file)
with open(csv_file, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["Timestamp", "Price"])
    writer.writerow([datetime.datetime.utcnow().isoformat(), price])
print(f"Saved latest price to {csv_file}")