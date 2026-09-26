# 🎮 Video Game Sales Market Analysis

Exploratory data analysis of global video game sales (1980–2016) to identify patterns that determine whether a game succeeds, and to support a 2017 marketing/campaign strategy for an online game store.

---

## 🎯 Objective

An online game store has historical data on game sales, user and critic reviews, genres, ESRB ratings, and platforms. The goal is to identify patterns that indicate whether a game is likely to succeed, so the store can plan its 2017 advertising campaigns and spot promising platforms.

This project answers the following questions:

- Which platforms are leading in sales? Which are growing or declining?
- Do the differences in sales across platforms matter?
- How do user and critic reviews affect sales on a given platform?
- What are the most profitable genres?
- How do user profiles (platforms, genres, ESRB ratings) differ across North America, Europe, and Japan?
- Are average user ratings the same across **Xbox One** and **PC**?
- Do average user ratings differ between **Action** and **Sports** genres?

---

## 🗂️ About the Data

The full dataset (`games.csv`) is not included in this repository (see `.gitignore`) to avoid publishing the raw data.

It contains:

- Game name
- Platform
- Release year
- Genre
- Sales by region (NA/EU/JP/Other)
- Critic score
- User score
- ESRB rating

A small sample, `data/sample_games.csv`, **is** committed to this repository so anyone can inspect the schema and understand the data structure without needing the full file.

To reproduce the full analysis, place the complete `games.csv` in the local `data/` folder (not tracked by Git) and point the notebook's `read_csv` call at it.

---

## 🛠️ Analysis Focus

The analysis focuses on:

1. **Platform sales performance**: identifying leading platforms and determining which are growing or declining.
2. **Platform lifecycle**: evaluating how long platforms remain active and which years are most representative of the market going into 2017.
3. **Sales distributions**: comparing game sales across platforms and assessing differences in their distributions.
4. **Review impact**: examining how critic and user scores relate to game sales.
5. **Genre performance**: identifying the most profitable game genres.
6. **Regional user profiles**: comparing platform, genre, and ESRB-rating preferences across North America, Europe, and Japan.
7. **Hypothesis testing**:
   - Comparing average user ratings for **Xbox One** and **PC**.
   - Comparing average user ratings for **Action** and **Sports** games.

---

## 🧰 Tech Stack

- Python 3
- Pandas
- NumPy
- Matplotlib
- SciPy (`scipy.stats` for Kruskal-Wallis and Welch's t-test)
- Jupyter Notebook / JupyterLab

---

## 📁 Repository Structure

```text
.
├── notebooks/
│   └── game_sales_analysis.ipynb
├── data/
│   ├── sample_games.csv   # Small sample, tracked in Git
│   └── games.csv          # Full dataset, local only, not tracked
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 How to Run This Project

### Using `venv`

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

### Using Conda

```bash
conda create -n game-sales-eda python=3.11
conda activate game-sales-eda
pip install -r requirements.txt
jupyter lab
```

---

## 📈 Key Findings

- **Platform lifecycle**: platforms have an average lifespan of approximately **11 years**. The market follows a clear generational succession pattern, so only recent data from **2013–2016** are representative of the current market going into 2017.
- **Promising platforms**: only **PS4** and **XOne** show a growth trend in the recent period, making them the most promising platforms for 2017 investment.
- **Sales distributions**: sales are heavily right-skewed for every platform, confirmed via the **Kruskal-Wallis test (p < 0.05)**. The median, rather than the mean, is therefore the more reliable measure of a typical game's performance.
- **Reviews and sales**: critic scores correlate moderately with sales, while user scores show little to no correlation.
- **Genre performance**: **Action, Shooter, Sports, and RPG** are the most profitable genres.
- **Regional differences**: regional profiles vary significantly. Japan, in particular, favors **Role-Playing games** and retains older consoles longer than North America or Europe.
- **Xbox One vs. PC ratings**: using 2013–2016 data, there is no significant difference in average user ratings between **Xbox One** and **PC** (`p ≈ 0.15`).
- **Action vs. Sports ratings**: average user ratings for **Action** and **Sports** games are significantly different (`p ≈ 1e-20`).

---

## 👤 Author

**Pedro LO Costa**

Project developed as part of my data analytics portfolio.

[LinkedIn](https://www.linkedin.com/in/pedrolocosta) · [GitHub](https://github.com/pedrolocosta)
