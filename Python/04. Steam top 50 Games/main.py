
# ---------------------------- IMPORTS ------------------------------- #

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

# ---------------------------- REQUEST CONFIGS ------------------------------- #
# steamcharts blocks default Python requests UA → fake a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
URL = "https://steamcharts.com/top"

# ---------------------------- SCRAPER ------------------------------- #
games = []

for page in range(1, 3):
    url = f"{URL}/p.{page}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Page {page} failed: HTTP {response.status_code} - {response.reason}")

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"id": "top-games"})
    rows = table.find_all("tr")

    for row in rows[1:]:  # Skip header row
        cells = row.find_all("td")
        games.append({
            "RANK": int(cells[0].text.strip().replace(".", "")),
            "NAME": cells[1].text.strip(),
            "CURRENT": int(cells[2].text.strip().replace(",", "")),
            "24H_PEAK": int(cells[4].text.strip().replace(",", "")),
            "ALL-TIME PEAK": int(cells[5].text.strip().replace(",", ""))
        })



# ---------------------------- OUTPUT ------------------------------- #
games_df = pd.DataFrame(games).set_index("RANK")
os.makedirs("output", exist_ok=True)
games_df.reset_index().to_json("output/top_games.json", orient="records", indent=2)


games_df["CURRENT"] = games_df["CURRENT"].astype("float64")
games_df["24H_PEAK"] = games_df["24H_PEAK"].astype("float64")
games_df["ALL-TIME PEAK"] = games_df["ALL-TIME PEAK"].astype("float64")

pd.options.display.float_format = '{:,.0f}'.format
print(games_df)
print(f"\n✅ {len(games_df)} games written to output/top_games.json")