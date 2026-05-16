import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.patches import FancyBboxPatch, Rectangle, Ellipse
from matplotlib.ticker import FuncFormatter
import os
import numpy as np


def create_language_usage_chart(
    start, end, time_spent, language_data, filename="lang_stats.svg"
):
    # Styling colors
    label_color = "#757A7F"
    annotation_color = "#757A7F"
    title_color = "#757A7F"

    df = pd.DataFrame(language_data, columns=["Language", "Percent", "Label"])
    df = df.sort_values("Percent", ascending=False).reset_index(drop=True)
    df["DisplayPercent"] = df["Percent"] ** 0.7

    colors = sns.color_palette("Set2", len(df), desat=0.8)

    sns.set_theme(style="white")
    sns.set_color_codes("pastel")

    fig, ax = plt.subplots(figsize=(8, 4))

    sns.barplot(
        data=df,
        x="DisplayPercent",
        y="Language",
        ax=ax,
        palette=colors,
    )

    new_patches = []
    for i, patch in enumerate(reversed(ax.patches)):
        bb = patch.get_bbox()
        p_bbox = FancyBboxPatch(
            (bb.xmin, bb.ymin),
            abs(bb.width),
            abs(bb.height),
            boxstyle="round,pad=0,rounding_size=0.15",
            ec="none",
            fc=colors[len(df) - 1 - i],
            mutation_aspect=1,
        )
        patch.remove()
        new_patches.append(p_bbox)

    for patch in new_patches:
        ax.add_patch(patch)

    max_val = max(df["DisplayPercent"])

    for i, (percent, display_percent, label) in enumerate(
        zip(df["Percent"], df["DisplayPercent"], df["Label"])
    ):
        ax.text(
            display_percent + max_val * 0.02,
            i,
            f"{label} ({percent:.2f}%)",
            va="center",
            ha="left",
            fontsize=10,
            fontweight="medium",
            color=annotation_color,
        )

    ax.set_yticklabels(ax.get_yticklabels(), color=label_color, fontsize=12)

    ax.text(
        0,
        1.15,
        "Languages",
        transform=ax.transAxes,
        fontsize=16,
        fontweight="bold",
        color=title_color,
    )

    ax.text(
        0,
        1.03,
        f"From {start} to {end} • Duration: {time_spent}",
        transform=ax.transAxes,
        fontsize=12,
        color=annotation_color,
    )

    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticks([])
    ax.tick_params(axis="both", which="both", length=0)

    max_val = max(df["DisplayPercent"])
    ax.set_xlim(0, max_val * 1.25)

    sns.despine(left=True, bottom=True)

    plt.tight_layout()

    os.makedirs("results", exist_ok=True)
    output_path = os.path.join(os.getcwd(), "results", filename)
    plt.savefig(output_path, format="svg", transparent=True)
    plt.close()


def create_weekly_summary_chart(stats, filename="day_wise_stats.svg"):
    dates = list(stats.keys())
    raw_usages = [sum(day.values()) for day in stats.values()]
    total_usage = sum(raw_usages)

    if total_usage == 0:
        usages = [0 for _ in raw_usages]
    else:
        usages = [(u / total_usage) * 100 for u in raw_usages]

    df = pd.DataFrame({"dates": dates, "usage": usages})[::-1]

    text_color = "#757A7F"
    sns.set_theme(style="whitegrid")
    colors = sns.color_palette("Paired", len(df))

    fig, ax = plt.subplots(figsize=(10, 5))

    df["hue"] = df["dates"]
    bars = sns.barplot(
        data=df, x="dates", y="usage", hue="hue", palette=colors, ax=ax, legend=False
    )

    bar_info = []
    for patch in bars.patches:
        bb = patch.get_bbox()
        bar_info.append(
            {
                "x": bb.xmin,
                "y": bb.ymin,
                "width": bb.width,
                "height": bb.height,
                "color": patch.get_facecolor(),
            }
        )
    for patch in bars.patches[:]:
        patch.remove()

    # Draw custom rounded bars with shadow
    for info in bar_info:
        bar_height = info["height"]
        width = info["width"]
        x = info["x"]
        y = info["y"]
        color = info["color"]

        ellipse_height = width * 20
        radius = ellipse_height / 2

        # Shadow
        ax.add_patch(
            Rectangle(
                (x + 0.05, y - 0.2),
                width,
                bar_height - radius,
                color="gray",
                alpha=0.3,
                zorder=0,
            )
        )
        ax.add_patch(
            Ellipse(
                (x + width / 2 + 0.05, y + bar_height - radius - 0.2),
                width=width,
                height=ellipse_height,
                color="gray",
                alpha=0.3,
                zorder=0,
            )
        )

        # Bar
        ax.add_patch(
            Rectangle(
                (x, y), width, bar_height - radius, color=color, linewidth=0, zorder=1
            )
        )
        ax.add_patch(
            Ellipse(
                (x + width / 2, y + bar_height - radius),
                width=width,
                height=ellipse_height,
                color=color,
                linewidth=0,
                zorder=2,
            )
        )

    ax.set_ylabel("Usage (%)", fontsize=12, color=text_color)
    ax.set_xlabel("")
    ax.set_title(
        "Weekly Usage Summary", fontsize=14, weight="bold", pad=20, color=text_color
    )
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.0f}%"))
    ax.set_ylim(0, max(usages) * 1.15 if usages else 1)
    ax.tick_params(axis="x", labelrotation=45, labelsize=10, colors=text_color)
    ax.tick_params(axis="y", labelsize=10, colors=text_color)

    for spine in ax.spines.values():
        spine.set_color(text_color)

    sns.despine(left=True, bottom=True)

    plt.tight_layout()

    os.makedirs("results", exist_ok=True)
    output_path = os.path.join(os.getcwd(), "results", filename)
    plt.savefig(output_path, format="svg", dpi=300, transparent=True)
    plt.close()


if __name__ == "__main__":
    mock_language_data = [
        ("Python", 42.35, "12 hrs 24 mins"),
        ("Rust", 21.80, "6 hrs 23 mins"),
        ("TypeScript", 14.10, "4 hrs 08 mins"),
        ("Go", 8.75, "2 hrs 34 mins"),
        ("C++", 5.40, "1 hr 35 mins"),
        ("Shell", 3.20, "56 mins"),
        ("Markdown", 2.10, "37 mins"),
        ("YAML", 1.30, "22 mins"),
    ]

    start = "2026-05-01"
    end = "2026-05-16"
    time_spent = "28 hrs 59 mins"

    create_language_usage_chart(
        start=start,
        end=end,
        time_spent=time_spent,
        language_data=mock_language_data,
        filename="../results/lang_stats.svg",
    )
