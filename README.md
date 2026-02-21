**Exploratory Data Analysis of Netflix Movies Released in the 1990s**

This project performs exploratory data analysis on Netflix movie data to understand patterns in film duration and genre trends during the 1990s decade. Using Python (pandas + matplotlib), we filter, analyze, and visualize movie attributes to support a production company researching nostalgic 90s film styles.

**Project Objectives**

Using the dataset netflix_data.csv, the analysis answers two key questions:

1. What was the most frequent movie duration in the 1990s?

A histogram is plotted for 1990s movie durations.
An approximate duration is saved as:

duration = 100

2. How many short action movies (under 90 minutes) were released in the 1990s?

A movie is considered short if duration < 90.

The count of short action movies is computed and stored as:

short_movie_count

**Dataset Description**

The dataset consists of one CSV file:

netflix_data.csv

**Files Included**

- README.md                  → Project documentation  

- netflix_data.csv           → Raw dataset  

- netflix_1990s_analysis.py  → Python script 

- duration_histogram.png      → Histogram of movie durations
  
- action_short_count.txt      → Number of short action movies
  
- netflix_1990s_movies.csv    → Filtered dataset (optional export)

**Key Results**

Metric	Result

Most frequent duration (approx)	100 minutes

Number of short action movies (<90 min)	short_movie_count
