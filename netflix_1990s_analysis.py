import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load dataset
netflix_df = pd.read_csv("netflix_data.csv")

# Filter movies only
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter movies released from 1990–1999
movies_1990s = netflix_subset[
    (netflix_subset["release_year"] >= 1990) &
    (netflix_subset["release_year"] < 2000)
]

# Plot histogram of movie durations
plt.hist(movies_1990s["duration"], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Movie Durations (1990s)")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()

# Save plot
plt.savefig(os.path.join(OUTPUT_DIR, "duration_histogram.png"), dpi=200)
plt.close()

# APPROXIMATE most frequent duration (modify manually based on histogram)
duration = 100  

# Filter for Action movies in the 1990s
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Count short action movies (< 90 mins)
short_movie_count = (action_movies_1990s["duration"] < 90).sum()

# Save outputs to CSV
pd.DataFrame({
    "approx_most_frequent_duration": [duration],
    "short_action_movie_count": [short_movie_count]
}).to_csv(os.path.join(OUTPUT_DIR, "1990s_movie_summary.csv"), index=False)

# Also save full filtered datasets (optional but good for GitHub)
movies_1990s.to_csv(os.path.join(OUTPUT_DIR, "movies_1990s.csv"), index=False)
action_movies_1990s.to_csv(os.path.join(OUTPUT_DIR, "action_movies_1990s.csv"), index=False)

print("Analysis complete! CSV files and plot saved in /outputs/")
