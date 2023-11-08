import pandas as pd
import json

# Here's an updated code snippet that uses the json.loads method and a try-except block to handle potential errors:
# This updated code should handle any malformed JSON strings by returning an empty list in case of errors while parsing. Make sure to adjust the column name 'json_data_column' to match the actual column name in your DataFrame.
# This code will create a new DataFrame, long_df, where each row contains the episode number, role, and name in long format

# Load your CSV file into a Pandas DataFrame
df = pd.read_csv("your_file.csv")


# Load your CSV file into a Pandas DataFrame
df = pd.read_csv("your_file.csv")


# Define a function to safely parse JSON
def parse_json(json_str):
    try:
        return json.loads(json_str)
    except (ValueError, TypeError):
        return []


# Apply the function to the column containing JSON data
df["json_data_column"] = df["json_data_column"].apply(parse_json)

# Create a new DataFrame in long format
long_format_data = []

for index, row in df.iterrows():
    episodenbr = row["episodenbr"]
    for item in row["json_data_column"]:
        role = item.get("role", "N/A")
        name = item.get("name", "N/A")
        long_format_data.append({"episodenbr": episodenbr, "role": role, "name": name})

long_df = pd.DataFrame(long_format_data)

# Now, you have a DataFrame in long format with 'episodenbr', 'role', and 'name' columns
print(long_df)
