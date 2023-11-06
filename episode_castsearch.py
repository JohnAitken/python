import pandas as pd
import tkinter as tk
from tkinter import Entry, Button, Label, Frame, Text, font
from prettytable import PrettyTable

result_frame = None

def display_results(data):
    global result_frame

    if result_frame is not None:
        result_frame.destroy()

    result_frame = Frame(root)
    result_frame.pack(fill='both', expand=True)

    text_box = Text(result_frame, wrap=tk.WORD)
    text_box.pack(fill='both', expand=True)
    text_box.tag_configure("header", font=("Arial", 14, "bold"))
    text_box.tag_configure("value", font=("Arial", 12))

    parts = data.split('\n')
    for part in parts:
        if "Episode Details" in part:
            text_box.insert(tk.END, part, "header")
        elif "Episode Summary" in part:
            text_box.insert(tk.END, part, "header")
        elif "The Cast" in part:
            text_box.insert(tk.END, part, "header")
        else:
            text_box.insert(tk.END, part, "value")
        text_box.insert(tk.END, "\n")

def filter_data():
    filter_value = filter_input.get().lower()
    jd['title'] = jd['title'].str.lower()
    filtered_df = jd[jd['title'] == filter_value]

    if not filtered_df.empty:
        details_output = "Episode Details:\n"
        details_df = filtered_df.iloc[:1].drop(['role', 'name', 'summary'], axis=1)

        # Create a PrettyTable for the "Episode Details" table
        details_table = PrettyTable()
        details_table.field_names = details_df.columns
        for _, row in details_df.iterrows():
            details_table.add_row(row)

        details_table.align = "l"  # Left-align all columns

        details_output += details_table.get_string() + "\n"

        summary_output = "Episode Summary:\n"
        summary_output += filtered_df['summary'].head(1).to_string(index=False) + "\n"

        cast_output = "The Cast:\n"
        cast_output += filtered_df[['role', 'name']].to_string(index=False)

        combined_output = details_output + summary_output + cast_output
        display_results(combined_output)
    else:
        display_results(f"No rows found with title equal to {filter_value}")

root = tk.Tk()
root.title("Search and Display")
root.geometry("800x600")

dwguide = pd.read_csv("dwguide_clean.csv")
castlist = pd.read_csv("castlist.csv")
jd = pd.merge(dwguide, castlist, how="left", on="episodenbr")

filter_input_label = Label(root, text="Enter the value to filter by:")
filter_input_label.pack()

filter_input = Entry(root)
filter_input.pack()

search_button = Button(root, text="Search", command=filter_data)
search_button.pack()

root.mainloop()
