from datetime import datetime
from pathlib import Path


def create_wakatime_summary_card(
    daily_avg: str,
    best_day_dict: dict,
    *,
    width: int = 420,
    height: int = 300,
    theme: str = "dark",
    layout: str = "vertical",
    output_file: str | None = None,
):
    best_day = datetime.strptime(
        best_day_dict["date"],
        "%Y-%m-%d",
    ).strftime("%d %b %Y")

    best_day_time = best_day_dict["text"]

    themes = {
        "dark": {
            "bg_color": "#1C1C1C",
            "border_color": "#30363D",
            "title_color": "#9CA3AF",
            "value_color": "#F5F7FA",
            "avg_accent": "#8A9DFF",
            "best_accent": "#92EFB4",
        },
        "light": {
            "bg_color": "#F3F4F6",
            "border_color": "#D0D7DE",
            "title_color": "#57606A",
            "value_color": "#111827",
            "avg_accent": "#5B6EFF",
            "best_accent": "#2DA44E",
        },
    }

    if theme not in themes:
        raise ValueError(f"Invalid theme '{theme}'. Use 'dark' or 'light'.")

    if layout not in {"vertical", "horizontal"}:
        raise ValueError(f"Invalid layout '{layout}'. Use 'vertical' or 'horizontal'.")

    colors = themes[theme]

    bg_color = colors["bg_color"]
    border_color = colors["border_color"]

    title_color = colors["title_color"]
    value_color = colors["value_color"]

    avg_accent = colors["avg_accent"]
    best_accent = colors["best_accent"]

    radius = 22

    avg_font_size = min(26, max(18, width / 16))
    best_font_size = min(24, max(16, width / 18))

    # -----------------------------
    # Layout calculations
    # -----------------------------
    if layout == "vertical":
        section_height = height / 2

        divider = f"""
        <line
            x1="28"
            y1="{section_height}"
            x2="{width - 28}"
            y2="{section_height}"
            stroke="{border_color}"
            stroke-width="1"
        />
        """

        accents = f"""
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
        """

        content = f"""
        <!-- Daily Average -->
        <text
            x="52"
            y="60"
            fill="{title_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="17"
            font-weight="500"
        >
            Daily Average
        </text>

        <text
            x="52"
            y="100"
            fill="{value_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="{avg_font_size}"
            font-weight="700"
        >
            {daily_avg}
        </text>

        <!-- Best Day -->
        <text
            x="52"
            y="{section_height + 55}"
            fill="{title_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="17"
            font-weight="500"
        >
            Best Day
        </text>

        <text
            x="52"
            y="{section_height + 85}"
            fill="{value_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="{best_font_size}"
            font-weight="700"
        >
            {best_day_time}
        </text>

        <text
            x="52"
            y="{section_height + 112}"
            fill="{title_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="15"
            font-weight="500"
        >
            {best_day}
        </text>
        """

    else:
        section_width = width / 2

        divider = f"""
        <line
            x1="{section_width}"
            y1="28"
            x2="{section_width}"
            y2="{height - 28}"
            stroke="{border_color}"
            stroke-width="1"
        />
        """

        accents = f"""
        <!-- Left Accent -->
        <rect
            x="28"
            y="36"
            width="7"
            height="{height - 72}"
            rx="4"
            fill="{avg_accent}"
        />

        <!-- Right Accent -->
        <rect
            x="{section_width + 28}"
            y="36"
            width="7"
            height="{height - 72}"
            rx="4"
            fill="{best_accent}"
        />
        """

        content = f"""
        <!-- Daily Average -->
        <text
            x="52"
            y="70"
            fill="{title_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="17"
            font-weight="500"
        >
            Daily Average
        </text>

        <text
            x="52"
            y="110"
            fill="{value_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="{avg_font_size}"
            font-weight="700"
        >
            {daily_avg}
        </text>

        <!-- Best Day -->
        <text
            x="{section_width + 52}"
            y="70"
            fill="{title_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="17"
            font-weight="500"
        >
            Best Day
        </text>

        <text
            x="{section_width + 52}"
            y="108"
            fill="{value_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="{best_font_size}"
            font-weight="700"
        >
            {best_day_time}
        </text>

        <text
            x="{section_width + 52}"
            y="132"
            fill="{title_color}"
            font-family="Inter, Segoe UI, sans-serif"
            font-size="15"
            font-weight="500"
        >
            {best_day}
        </text>
        """

    # -----------------------------
    # Default filename
    # -----------------------------
    if output_file is None:
        output_file = f"stats_card_{theme}.svg"

    # -----------------------------
    # SVG
    # -----------------------------
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

        {divider}

        {accents}

        {content}

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
        layout="vertical",
    )

    create_wakatime_summary_card(
        daily_avg="5 hrs 12 mins",
        best_day_dict={
            "date": "2026-05-10",
            "text": "9 hrs 41 mins",
        },
        theme="light",
        layout="horizontal",
        width=700,
        height=180,
    )
