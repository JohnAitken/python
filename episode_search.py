import pandas as pd
from tabulate import tabulate


dwguide = pd.read_csv("dwguide_clean.csv")
castlist = pd.read_csv("castlist.csv")

jd = pd.merge(dwguide, castlist, how="left", on="episodenbr")

# Ask the user for the value to filter by (and convert it to lowercase)
filter_value = input("Enter the value to filter by: ").lower()

# Convert the values in the 'Name' column to lowercase for case-insensitive comparison
jd['title'] = jd['title'].str.lower()

# Filter the DataFrame while ignoring case differences
filtered_df = jd[jd['title'] == filter_value]

# Display the first row of the filtered DataFrame (excluding 'role' and 'name' columns)
if not filtered_df.empty:
    print("Episode summary")
    filtered_df_1 = filtered_df.iloc[:1].drop(['role', 'name'], axis=1)
    print(tabulate(filtered_df_1, headers='keys', tablefmt='fancy_grid'))

    # Display the 'name' and 'role' columns for the entire filtered DataFrame
    print("\nThe Cast:")
    filtered_df_2 = filtered_df[['name', 'role']]
    print(tabulate(filtered_df_2, headers='keys', tablefmt='fancy_grid'))
else:
    print(f"No rows found with title equal to {filter_value}")