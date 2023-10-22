import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('booklist_data.csv')

# Randomly select a row based on 'File_Name'
random_row = df.sample(n=1, random_state=42)

# Get the 'File_Path' value from the randomly selected row
file_path = random_row['File_Path'].values[0]

# Print the randomized 'File_Name' and the corresponding 'File_Path' content
print(f'Random File_Name: {random_row["File_Name"].values[0]}')
print(f'File_Path Content: {file_path}')
