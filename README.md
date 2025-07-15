<img width="1000" height="353" alt="Wakadash (2)" src="media/Wakadash.png" />

## WakaDash

Tool that fetches your weekly [WakaTime](https://wakatime.com/) coding statistics and generates  charts. You can embed this visual breakdown anywhere - from your GitHub profile README to a personal portfolio.


<p align="center">
  <img src="results/lang_stats.png" alt="WakaTime Language Usage Chart" width="600">
</p>


<p align="center">
  <img src="results/day_wise_stats.png" alt="Weekly usage summary Chart" width="1000">
</p>

## Badges
<p align="left">
  <img src="results/best_badge.svg" alt="Best badge" width="430">
</p>

<p align="left">
  <img src="results/daily_avg_badge.svg" alt="Daily avg badge" width="300">
</p>

##  Use This in Your Own Profile (Fork & Go!) 🍴

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


4. The action will now run automatically once per day, and generate a new lang_stats.png
or you can run it manually by clicking here.

<img width="756" height="462" alt="image" src="media/ins3.png" />


### Step 5: Show It in Your GitHub Profile

In your Profile `Readme.md`, paste this:

Replace `<your-username>` with your user-name.

```md
![WakaTime Stats](https://raw.githubusercontent.com/<your-username>/WakaDash/main/lang_stats.png)

```

✅ That's it! Every day your chart will auto-update with your latest WakaTime stats.

