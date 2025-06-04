import pandas as pd
from datetime import datetime, timedelta

# Load dataset with trending_date as datetime (already fixed)
df = pd.read_csv("cleaned_data/youtube_trending_ready.csv", parse_dates=['trending_date'])

print(f"📅 Max trending date in data: {df['trending_date'].max()}")

# Filter data to last 6 months from max trending date
max_date = df['trending_date'].max()

if pd.isna(max_date):
    print("No valid trending_date found, cannot filter by date.")
    filtered_df = df.copy()
else:
    six_months_ago = max_date - timedelta(days=180)
    filtered_df = df[df['trending_date'] >= six_months_ago]
    print(f"Filtered rows: {len(filtered_df)}")

# If no rows after filtering, use all rows
if len(filtered_df) == 0:
    print("Only 0 rows available after filtering. Using all rows.")
    filtered_df = df.copy()

# Sample 20,000 rows if data is large
sample_size = 20000
if len(filtered_df) > sample_size:
    filtered_df = filtered_df.sample(n=sample_size, random_state=42)
    print(f"Sampled down to {sample_size} rows.")

# Save filtered data to CSV
filtered_df.to_csv("cleaned_data/youtube_trending_filtered.csv", index=False)
print("✅ Filtered CSV saved as 'youtube_trending_filtered.csv'")
