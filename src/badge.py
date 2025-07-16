import requests
from datetime import datetime
import os


def create_wakatime_badges(
    daily_avg_sec: int,
    best_day_dict: dict,
    avg_badge_right_color: str,
    best_badge_right_color: str,
    avg_badge_left_color: str,
    best_badge_left_color: str,
    badge_style: str,
):
    daily_avg = daily_avg_sec
    best_day = datetime.strptime(best_day_dict.get("date"), "%Y-%m-%d").strftime(
        "%d %B %Y"
    )
    best_day_time = best_day_dict.get("text")

    avg_label = f"Daily_average-{daily_avg}"
    best_label = f"Best day-{best_day_time} on {best_day}"

    avg_label_encoded = avg_label.replace(" ", "_")
    best_label_encoded = best_label.replace(" ", "_")

    daily_avg_response = requests.get(
        f"https://img.shields.io/badge/{avg_label_encoded}-{avg_badge_right_color}?style={badge_style}&labelColor={avg_badge_left_color}"
    )
    daily_avg_response.raise_for_status()

    best_response = requests.get(
        f"https://img.shields.io/badge/{best_label_encoded}-{best_badge_right_color}?style={badge_style}&labelColor={best_badge_left_color}"
    )
    best_response.raise_for_status()

    os.makedirs("results", exist_ok=True)

    with open(os.path.join(os.getcwd(), "results", "daily_avg_badge.svg"), "wb") as f:
        f.write(daily_avg_response.content)

    with open(os.path.join(os.getcwd(), "results", "best_badge.svg"), "wb") as f:
        f.write(best_response.content)
