# 📊 YouTube Trending Video Analytics

A data analytics project that explores global YouTube trending videos to understand what types of content go viral, for how long, and across which regions. This end-to-end project includes data cleaning, sentiment analysis, SQL queries, time-series insights, and an interactive Power BI dashboard.

---

## Objectives

- Analyze trending video patterns across countries (IN, US, GB, CA)
- Perform sentiment analysis on titles and tags
- Rank video categories by average views
- Visualize time-based trends (publish vs trending date)
- Create a multi-page Power BI dashboard for storytelling

---

## 🔧 Tools & Technologies

- **Python** – Data Cleaning, Sentiment Analysis (`pandas`, `textblob`, `seaborn`)
- **Oracle SQL And SQL Developer** – Data exploration, aggregation, and ranking
- **Power BI** – Dashboard creation and visual analytics
- **Datasets** – YouTube trending video data (`.csv`) and category metadata (`.json`) from Kaggle

---

## 📁 Project Structure

```
📦 youtube-trending-video-analytics/
│
├── cleaned_data/
│   └── youtube_trending_filtered.csv         # Filtered final dataset (~20K rows)
│
├── Dashboard/
│   ├── YouTube Trending Video Analytics.pbix # Power BI Dashboard
│   └── *.png                                 # Screenshots of each page
│
├── python_queries/
│   └── cleaning_script.ipynb / .py           # Python code for cleaning, merging, filtering
│
├── Sql_Queries_Outputs/
│   └── *.png                                 # Output screenshots of executed SQL queries
```

---

## 📊 Power BI Dashboard Pages

1. **Executive Summary** – KPIs (views, video counts, top region)
2. **Genre & Sentiment** – Sentiment distribution and category analysis by region
3. **Time Series** – Publishing and trending date patterns over time

Includes **interactive filters** for region, category, and sentiment.

---

## 🔍 Key Analytical Highlights

- Most popular categories globally and regionally
- Sentiment breakdown: Positive, Neutral, Negative
- Top trending videos by view count
- Region-wise average likes and viewer engagement
- Trend durations and content publishing patterns

---

## 📝 Final Deliverables

- Cleaned and filtered datasets
- Python scripts for preprocessing and sentiment
- SQL queries with results
- Power BI `.pbix` file and dashboard screenshots
- Final 2-page project report (not included in repo)

