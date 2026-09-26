# Video Game Sales Market Analysis

Exploratory data analysis of global video game sales (1980–2016) to identify patterns that
determine whether a game succeeds, and to support a 2017 marketing/campaign strategy for an
online game store.

## Business Task

An online game store has historical data on game sales, user and critic reviews, genres, ESRB
ratings, and platforms. The goal is to identify patterns that indicate whether a game is likely
to succeed, so the store can plan its 2017 advertising campaigns and spot promising platforms.

## Key Questions Answered

- Which platforms are leading in sales? Which are growing or declining?
- Do the differences in sales across platforms matter?
- How do user and critic reviews affect sales on a given platform?
- What are the most profitable genres?
- How do user profiles (platforms, genres, ESRB ratings) differ across North America, Europe,
  and Japan?
- Hypothesis testing: are average user ratings the same across Xbox One and PC? Do they differ
  between Action and Sports genres?

## Data

The dataset (`games.csv`) is not included in this repository (see `.gitignore`). It contains
game name, platform, release year, genre, sales by region (NA/EU/JP/Other), critic score, user
score, and ESRB rating.

To run this project, place `games.csv` in a local `data/` folder (not tracked by git).

## Tech Stack

- Python 3
- pandas, numpy — data wrangling
- scipy.stats — hypothesis testing (Kruskal-Wallis, Welch's t-test)
- matplotlib — visualization
- Jupyter Notebook / JupyterLab

## Project Structure

```
.
├── notebooks/
│   └── game_sales_analysis.ipynb
├── data/                  # local only, not tracked
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

## Key Findings

- Platforms have an average lifespan of ~11 years; the market follows a clear generational
  succession pattern, so only recent years' data (2013–2016) are representative of the current
  market going into 2017.
- Only **PS4** and **XOne** show a growth trend in the recent period — the most promising
  platforms for 2017 investment.
- Sales are heavily right-skewed for every platform (confirmed via Kruskal-Wallis test,
  p < 0.05); median, not mean, is the reliable measure of a "typical" game's performance.
- Critic scores correlate moderately with sales; user scores show little to no correlation.
- Action, Shooter, Sports, and RPG are the most profitable genres, though regional profiles
  vary significantly — Japan in particular favors Role-Playing games and retains older consoles
  longer than North America or Europe.
- Hypothesis testing (2013–2016 data): no significant difference in average user ratings between
  Xbox One and PC (p ≈ 0.15); Action and Sports genres do show significantly different average
  user ratings (p ≈ 1e-20).

## Author

Pedro [Last Name] — Mechanical Engineer transitioning to AI/Data Engineering.
[LinkedIn] · [GitHub]
