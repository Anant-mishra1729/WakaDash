from datetime import datetime
from pathlib import Path


def create_wakatime_summary_card(
    daily_avg: str,
    best_day_dict: dict,
    *,
    width: int = 420,
    height: int = 300,
    theme: str = "dark",
    output_file: str | None = None,
):
    best_day = datetime.strptime(
        best_day_dict["date"],
        "%Y-%m-%d",
    ).strftime("%d %b %Y")

    best_day_time = best_day_dict["text"]
    themes = {
        "dark": {
            "bg_color": "#121212",
            "border_color": "#30363D",
            "title_color": "#A8A8A8",
            "value_color": "#E6EDF3",
            "avg_accent": "#8A9DFF",
            "best_accent": "#92EFB4",
        },
        "light": {
            "bg_color": "#FFFFFF",
            "border_color": "#D0D7DE",
            "title_color": "#57606A",
            "value_color": "#1F2328",
            "avg_accent": "#5B6EFF",
            "best_accent": "#2DA44E",
        },
    }

    if theme not in themes:
        raise ValueError(f"Invalid theme '{theme}'. Use 'dark' or 'light'.")

    colors = themes[theme]

    bg_color = colors["bg_color"]
    border_color = colors["border_color"]

    title_color = colors["title_color"]
    value_color = colors["value_color"]

    avg_accent = colors["avg_accent"]
    best_accent = colors["best_accent"]

    radius = 22
    section_height = height / 2

    avg_font_size = min(25, max(20, width / 14))
    best_font_size = min(25, max(20, width / 14))

    # Default output filename
    if output_file is None:
        output_file = f"wakatime_summary_{theme}.svg"

    svg = f"""
    <svg
        width="{width}"
        height="{height}"
        viewBox="0 0 {width} {height}"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
    >

        <!-- Background -->
        <rect
            x="1"
            y="1"
            width="{width - 2}"
            height="{height - 2}"
            rx="{radius}"
            fill="{bg_color}"
            stroke="{border_color}"
            stroke-width="1.2"
        />

        <!-- Divider -->
        <line
            x1="28"
            y1="{section_height}"
            x2="{width - 28}"
            y2="{section_height}"
            stroke="{border_color}"
            stroke-width="1"
        />

        <!-- Daily Average Accent -->
        <rect
            x="28"
            y="32"
            width="7"
            height="{section_height - 64}"
            rx="4"
            fill="{avg_accent}"
        />

        <!-- Best Day Accent -->
        <rect
            x="28"
            y="{section_height + 32}"
            width="7"
            height="{section_height - 64}"
            rx="4"
            fill="{best_accent}"
        />

        <!-- Daily Average Title -->
        <text
            x="52"
            y="58"
            fill="{title_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="18"
            font-weight="500"
        >
            Daily Average
        </text>

        <!-- Daily Average Value -->
        <text
            x="52"
            y="98"
            fill="{value_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="{avg_font_size}"
            font-weight="700"
        >
            {daily_avg}
        </text>

        <!-- Best Day Title -->
        <text
            x="52"
            y="{section_height + 58}"
            fill="{title_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="18"
            font-weight="500"
        >
            Best Day
        </text>

        <!-- Best Day Value -->
        <text
            x="52"
            y="{section_height + 92}"
            fill="{value_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="{best_font_size}"
            font-weight="700"
        >
            {best_day_time + "  ●  " + best_day}
        </text>

    </svg>
    """

    # -----------------------------
    # Save SVG
    # -----------------------------
    Path("results").mkdir(exist_ok=True)

    with open(
        Path("results") / output_file,
        "w",
        encoding="utf-8",
    ) as f:
        f.write(svg)

    print(f"Saved: results/{output_file}")


if __name__ == "__main__":
    create_wakatime_summary_card(
        daily_avg="5 hrs 12 mins",
        best_day_dict={
            "date": "2026-05-10",
            "text": "9 hrs 41 mins",
        },
        theme="dark",
    )

    create_wakatime_summary_card(
        daily_avg="5 hrs 12 mins",
        best_day_dict={
            "date": "2026-05-10",
            "text": "9 hrs 41 mins",
        },
        theme="light",
    )
