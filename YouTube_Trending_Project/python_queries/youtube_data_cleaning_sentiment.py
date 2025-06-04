import pandas as pd
import json
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# =======================
# SETTINGS & PATHS
# =======================
countries = ['IN', 'US', 'GB', 'CA']
base_path = 'data/'
cleaned_path = 'cleaned_data/'
os.makedirs(cleaned_path, exist_ok=True)

# =======================
# HELPER FUNCTIONS
# =======================

# Function to load and clean one country file
def load_country_data(country_code):
    csv_path = os.path.join(base_path, f"{country_code}_youtube_trending_data.csv")
    json_path = os.path.join(base_path, f"{country_code}_category_id.json")

    # Load CSV
    df = pd.read_csv(csv_path)
    df.columns = [col.lower() for col in df.columns]  # standardize column names

    # Rename columns to unify format
    rename_map = {
        'view_count': 'views',
        'like_count': 'likes',
        'dislike_count': 'dislikes',
        'comment_count': 'comment_count',
    }
    df.rename(columns=rename_map, inplace=True)

    # Load category mapping
    with open(json_path, 'r') as f:
        categories = json.load(f)
    cat_map = {int(item['id']): item['snippet']['title'] for item in categories['items']}

    # Standardize columns
    df['categoryid'] = pd.to_numeric(df['categoryid'], errors='coerce')
    df['category_name'] = df['categoryid'].map(cat_map)
    df['region'] = country_code

    # Fix dates
    df['publishedat'] = pd.to_datetime(df.get('publishedat', pd.NaT), errors='coerce')
    df['trending_date'] = pd.to_datetime(df.get('trending_date', pd.NaT), format='%y.%d.%m', errors='coerce')

    # Convert numeric columns
    num_cols = ['views', 'likes', 'dislikes', 'comment_count']
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            df[col] = pd.NA  # add column if missing

    return df

# =======================
# STEP 1: LOAD + CLEAN ALL
# =======================
dfs = [load_country_data(code) for code in countries]
df = pd.concat(dfs, ignore_index=True)

# =======================
# STEP 2: SENTIMENT ANALYSIS
# =======================
analyzer = SentimentIntensityAnalyzer()
df['text_for_sentiment'] = df['title'].astype(str) + ' ' + df['tags'].astype(str)

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        return 'Positive'
    elif compound <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment_score'] = df['text_for_sentiment'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
df['sentiment'] = df['text_for_sentiment'].apply(get_sentiment)

# =======================
# OPTIONAL: REORDER COLUMNS
# =======================
ordered_cols = [
    "title", "categoryid", "category_name", "views", "likes", "dislikes", "comment_count",
    "publishedat", "trending_date", "region", "tags",
    "text_for_sentiment", "sentiment", "sentiment_score"
]
df = df[[col for col in ordered_cols if col in df.columns]]

# =======================
# FINAL SAVE
# =======================
df.to_csv(os.path.join(cleaned_path, "youtube_trending_ready.csv"), index=False)
print("✅ Final cleaned dataset saved as 'youtube_trending_ready.csv'")
print(df.head())
