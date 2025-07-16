import requests
import time
from datetime import datetime, timedelta, timezone
from collections import defaultdict


class WakaTimeClient:
    def __init__(self, api_key=None, range="last_7_days"):
        self.API_KEY = api_key
        self.STATS_RANGE = range

        if not self.API_KEY:
            raise ValueError("WAKATIME API KEY not found!")

    def weekly_summary(self):
        summaries = {}

        for i in range(1, 8):
            date = (datetime.now(timezone.utc) - timedelta(days=i)).strftime("%Y-%m-%d")
            url = f"https://wakatime.com/api/v1/users/current/durations?date={date}&api_key={self.API_KEY}"

            try:
                response = requests.get(url)
                response.raise_for_status()
                sessions = response.json().get("data", [])

                project_totals = defaultdict(float)
                for s in sessions:
                    project = s.get("project")
                    duration = s.get("duration", 0)
                    if project and duration:
                        project_totals[project] += duration

                summaries[date] = dict(project_totals)
                print(f"Fetched: {date}")

            except Exception as e:
                print(f"Error fetching {date}: {e}")
                summaries[date] = {}

            time.sleep(1)
        return summaries

    def fetch_stats(self):
        response = requests.get(
            f"https://wakatime.com/api/v1/users/current/stats/{self.STATS_RANGE}?api_key={self.API_KEY}"
        )
        response.raise_for_status()
        return response.json()["data"]

    def languages(self, data, limit=5):
        return [
            (lang["name"], lang["percent"], lang["text"])
            for lang in data.get("languages", [])[:limit]
        ]
