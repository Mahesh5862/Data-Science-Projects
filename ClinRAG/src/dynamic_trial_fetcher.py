import requests
import json


def fetch_trials(condition, save_path):
    query_term = condition.split(",")[0].strip()

    url = f"https://clinicaltrials.gov/api/v2/studies?query.term={query_term}&pageSize=50"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"Trials for '{query_term}' downloaded successfully.")
    else:
        print("Failed to fetch trials.")