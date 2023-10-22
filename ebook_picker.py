import webbrowser
import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox

# Read the CSV file
df = pd.read_csv('booklist_data.csv')

# Randomly select a row based on 'File_Name'
random_row = df.sample(n=1, random_state=42)

# Get the 'File_Name' and 'File_Path' values from the randomly selected row
file_name = random_row['File_Name'].values[0]
file_path = random_row['File_Path'].values[0]

# Create a function to open a popup with a clickable hyperlink
def open_popup():
    popup = tk.Tk()
    popup.title('Random ebook selector')
    label = tk.Label(popup, text=f'Random File Name: {file_name}')
    label.pack()
    hyperlink = tk.Label(popup, text='Click here to open the file')
    hyperlink.pack()
    hyperlink.bind("<Button-1>", lambda event: open_file(file_path))
    popup.mainloop()

# Function to open the file when the hyperlink is clicked
def open_file(file_path):
    webbrowser.open(file_path)
    # For example, you can use the webbrowser module to open URLs in the default web browser.

# Display the popup with the clickable hyperlink
open_popup()
