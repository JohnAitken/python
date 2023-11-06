import pandas as pd
from tabulate import tabulate
import tkinter as tk
from tkinter import simpledialog
from tkinter import Text

def main():
    dwguide = pd.read_csv("dwguide_clean.csv")
    castlist = pd.read_csv("castlist.csv")

    jd = pd.merge(dwguide, castlist, how="left", on="episodenbr")

    filter_value = simpledialog.askstring("Input", "Enter the value to filter by: ").lower()

    jd['title'] = jd['title'].str.lower()
    filtered_df = jd[jd['title'] == filter_value]

    if not filtered_df.empty:
        # Create a pop-up dialog
        popup = tk.Toplevel()
        popup.title("Episode Details")

        # Create an input field at the top
        input_label = tk.Label(popup, text="Filter Value:")
        input_label.pack()

        input_text = tk.Entry(popup)
        input_text.insert(0, filter_value)
        input_text.config(state="readonly")
        input_text.pack()

        # Display Episode Details
        details_output = "Episode Details:\n"
        filtered_df_1 = filtered_df.iloc[:1].drop(['role', 'name', 'summary'], axis=1)
        details_output += tabulate(filtered_df_1, headers='keys', tablefmt='grid') + "\n"

        # Display Episode Summary
        summary_output = "Episode Summary:\n"
        filtered_df_2 = filtered_df[['summary']].head(1)
        summary_output += tabulate(filtered_df_2, headers='keys', tablefmt='grid') + "\n"

        # Display The Cast
        cast_output = "The Cast:\n"
        filtered_df_3 = filtered_df[['role', 'name']]
        cast_output += tabulate(filtered_df_3, headers='keys', tablefmt='fancy_grid')

        combined_output = details_output + summary_output + cast_output

        # Create a text box to display the results below the input field
        text_box = Text(popup, height=20, width=80)
        text_box.insert(tk.END, combined_output)
        text_box.pack()
    else:
        tk.messagebox.showinfo("Info", f"No rows found with title equal to {filter_value}")

if __name__ == "__main__":
    main()
