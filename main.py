from src.wakatime import WakaTimeClient
from datetime import datetime, timedelta
from src.graph import create_language_usage_chart, create_weekly_summary_chart
from src.badge import create_wakatime_badges
import json
import os

with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Wakatime stats
waka = WakaTimeClient(os.getenv("WAKATIME_API_KEY"), config["stats_range"])
stats = waka.fetch_stats()

# Lanugage stats
create_language_usage_chart(
    (
        datetime.strptime(stats["start"], "%Y-%m-%dT%H:%M:%SZ") + timedelta(days=1)
    ).strftime("%d %B %Y"),
    datetime.strptime(stats["end"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d %B %Y"),
    stats["human_readable_total_including_other_language"],
    waka.languages(stats),
)

# Weekly summary
weekly_stats = waka.weekly_summary()
create_weekly_summary_chart(weekly_stats)

# Wakatime badga
create_wakatime_badges(
    daily_avg_sec=stats["human_readable_daily_average"],
    best_day_dict=stats["best_day"],
    avg_badge_left_color=config["badges"]["avg_badge_left_color"],
    avg_badge_right_color=config["badges"]["avg_badge_right_color"],
    best_badge_left_color=config["badges"]["best_badge_left_color"],
    best_badge_right_color=config["badges"]["best_badge_right_color"],
    badge_style=config["badges"]["badge_style"],
)
