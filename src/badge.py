import requests
from datetime import datetime
import os

def create_wakatime_badge(daily_avg_sec: int, best_day_dict: dict):
    daily_avg = daily_avg_sec
    best_day = datetime.strptime(best_day_dict.get("date"),"%Y-%m-%d").strftime("%d %B %Y")
    best_day_time = best_day_dict.get("text")

    avg_label = f"Daily_average-{daily_avg}"
    best_label = f"Best day-{best_day_time} on {best_day}"
    avg_color = "orange"
    best_color = "green"
    print(avg_label,best_label)

    avg_label_encoded = avg_label.replace(" ", "_")
    best_label_encoded = best_label.replace(" ", "_")
    print(avg_label_encoded,best_label_encoded)

    # Fetch and save badge
    daily_avg_response = requests.get(f"https://img.shields.io/badge/{avg_label_encoded}-{avg_color}?style=flat-square")
    daily_avg_response.raise_for_status()

    best_response = requests.get(f"https://img.shields.io/badge/{best_label_encoded}-{best_color}?style=flat-square")
    best_response.raise_for_status()

    os.makedirs("results",exist_ok= True)

    with open(os.path.join(os.getcwd(),"results","daily_avg_badge.svg"), "wb") as f:
        f.write(daily_avg_response.content)

    with open(os.path.join(os.getcwd(),"results","best_badge.svg"), "wb") as f:
        f.write(best_response.content)



