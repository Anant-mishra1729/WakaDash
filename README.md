<img width="1000" height="353" alt="Wakadash (2)" src="media/Wakadash.png" />

## WakaDash

Tool that fetches your weekly [WakaTime](https://wakatime.com/) coding statistics and generates charts. You can embed this visual breakdown anywhere - from your GitHub profile README to a personal portfolio.

## Language stats
<p align="center">
  <img src="results/lang_stats.svg" alt="WakaTime Language Usage Chart" width="800" height = "400">
</p>

## Weekly stats
<p align="center">
  <img src="results/day_wise_stats.svg" alt="Weekly usage summary Chart" width="1000">
</p>

## Badges
<p align="left">
  <img src="results/best_badge.svg" alt="Best badge" width="430">
</p>

<p align="left">
  <img src="results/daily_avg_badge.svg" alt="Daily avg badge" width="300">
</p>

<br />


##  Use This in Your Own Profile

You can use WakaDash to show your own coding activity by just forking this repo and connecting your WakaTime account. Here's how:


### Step 1: Create a Waktime account 
Go to [WakaTime](https://wakatime.com/), create your account and get your API Key.

### Step 2:  Fork This Repo

Click the "Fork" button in the top right of this page and fork it to your account.

### Step 3: Add Your WakaTime API Key as a Secret
1. Go to your forked repo’s `Settings` → `Secrets and variables` → `Actions` → `New repository secret`

2. Name the secret exactly: **`WAKATIME_API_KEY`**

3. Paste your WakaTime API Key 

###  Step 4: Enable GitHub Actions
1. Go to the `Actions` tab in your forked repo

2. Enable workflows if prompted

<img width="757" height="466" alt="image" src="media/ins1.png" />

<img width="756" height="462" alt="image" src="media/ins2.png" />


4. The action will now run automatically once per day, and generate a new lang_stats.svg
or you can run it manually by clicking here.

<img width="756" height="462" alt="image" src="media/ins3.png" />


### Step 5: Show It in Your GitHub Profile

In your Profile `Readme.md`, paste this:

Replace `<your-username>` with your user-name.

```md
![Language Stats](https://raw.githubusercontent.com/<your-username>/WakaDash/main/results/lang_stats.svg)

![Weekly Stats](https://raw.githubusercontent.com/<your-username>/WakaDash/main/results/day_wise_stats.svg)

![Best Day Badge](https://raw.githubusercontent.com/<your-username>/WakaDash/main/results/best_badge.svg)

![Daily Avg Badge](https://raw.githubusercontent.com/<your-username>/WakaDash/main/results/daily_avg_badge.svg)

```

 That's it! Every day your chart will auto-update with your latest WakaTime stats.

<br />

## Configuration

All stats are fully configurable by modifying the `config.json` file. Below are the customizable options:

### Wakatime stats range

`last_7_days`, `last_30_days`, `last_6_months`, `last_year`, or `all_time`

```json
"stats_range": "last_7_days",
```


### Badges 
Badges are powered by [Shields.io](https://shields.io/badges), so all customization options supported by Shields are available here.

#### Colors
You can customize the background color of the left and right parts of each badge using hex codes, RGB, RGBA, HSL, HSLA, or CSS named colors:

```json
"best_badge_right_color": "yellowgreen"
"best_badge_left_color": "grey"
"avg_badge_right_color": "tomato"
"avg_badge_left_color": "grey"
```

#### Badge style
Control the overall style of the badges.


```json
"badge_style": "flat-square"
```

Available styles:

* `flat`

<p align="left">
  <img src="https://img.shields.io/badge/Daily_average-25_mins-blue?style=flat" alt="Best badge" width="200">
</p>

* `flat-square` (default)

<p align="left">
  <img src="https://img.shields.io/badge/Daily_average-25_mins-gold?style=flat-square" alt="Best badge" width="200">
</p>

* `plastic`

<p align="left">
  <img src="https://img.shields.io/badge/Daily_average-25_mins-lightblue?style=plastic" alt="Best badge" width="200">
</p>


* `for-the-badge`

<p align="left">
  <img src="https://img.shields.io/badge/Daily_average-25_mins-chartreuse?style=for-the-badge" alt="Best badge" width="200">
</p>

* `social`

<p align="left">
  <img src="https://img.shields.io/badge/Daily_average-25_mins-chartreuse?style=social" alt="Best badge" width="200">
</p>
