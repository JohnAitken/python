import pandas as pd
import random
import tkinter as tk
import webbrowser

# Read the CSV file
df = pd.read_csv('booklist_data.csv')

# Initialize the random_row variable
random_row = None

# Function to randomize and select a row
def randomize_and_select():
    global random_row
    random_row = df.sample(n=1, random_state=random.randint(0, 9999))
    update_display()

# Function to update the display with the new random row
def update_display():
    if random_row is not None:
        file_name = random_row['File_Name'].values[0]
        file_path = random_row['File_Path'].values[0]
        label.config(text=f'Random File Name:       {file_name}')
        hyperlink.config(text='Click here to open the file', cursor='hand2')
        hyperlink.bind('<Button-1>', lambda event: open_file(file_path))

# Function to open the URL in a web browser when clicked
def open_file(file_path):
    webbrowser.open(file_path)

# Create a GUI window
root = tk.Tk()
root.title('Random Ebook Picker')

# Set a fixed width for the popup window
root.geometry("600x100")  # Adjust the width as needed

# Create a label for the text
label = tk.Label(root, text='', padx=10, pady=10)
label.pack()

# Add a clickable hyperlink
hyperlink = tk.Label(root, text='', fg='blue')
hyperlink.pack()

# Add a button to re-randomize
randomize_button = tk.Button(root, text='Re-Randomize', command=randomize_and_select)
randomize_button.pack()

# Initial randomization
randomize_and_select()


# Start the main GUI loop
root.mainloop()
