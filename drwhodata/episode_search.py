import pandas as pd

dwguide = pd.read_csv("dwguide_clean.csv")
castlist = pd.read_csv("castlist.csv")

jd = pd.merge(dwguide, castlist, how="left", on="episodenbr")

# Ask the user for the value to filter by (and convert it to lowercase)
filter_value = input("Enter the value to filter by: ").lower()

# Convert the values in the 'Name' column to lowercase for case-insensitive comparison
jd['Name'] = jd['title'].str.lower()

# Filter the DataFrame while ignoring case differences
filtered_df = jd[jd['title'] == filter_value]

# Display the result
if not filtered_df.empty:
    print("Filtered DataFrame:")
    print(filtered_df)
else:
    print(f"No rows found with Name equal to {filter_value}")