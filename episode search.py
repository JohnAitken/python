import pandas as pd
from tabulate import tabulate
from fuzzywuzzy import fuzz

# Load the data from CSV files
dwguide = pd.read_csv("dwguide_clean.csv")
castlist = pd.read_csv("castlist.csv")

# Merge the data
jd = pd.merge(dwguide, castlist, how="left", on="episodenbr")

# Ask the user for the value to search for (without knowing the exact spelling)
search_value = input("Enter the value to search for: ").lower()

# Define a threshold for fuzzy string matching
threshold = 70  # Adjust this threshold as needed

# Use fuzzy string matching to find approximate matches
jd['title_similarity'] = jd['title'].apply(lambda x: fuzz.token_set_ratio(search_value, x.lower()))
filtered_df = jd[jd['title_similarity'] >= threshold]

# Check if the searched string exists within the title
contains_search_value = jd[jd['title'].str.lower().str.contains(search_value)]

# Drop duplicates based on the 'title' column to keep only one row per match
filtered_df = filtered_df.drop_duplicates(subset=['title'])

# Print the total number of matches
total_matches = len(filtered_df) + len(contains_search_value)
if total_matches > 0:
    print(f"Total Matches Found: {total_matches}\n")

    if not filtered_df.empty:
        print(f"Approximate Matches (with similarity >= {threshold}%):")
        print(tabulate(filtered_df, headers='keys', tablefmt='simple'))
    
    if not contains_search_value.empty:
        print(f"\nExact Matches (title contains '{search_value}'):")
        print(tabulate(contains_search_value, headers='keys', tablefmt='fancy_grid'))
else:
    print(f"No matches found for '{search_value}'")
