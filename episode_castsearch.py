import pandas as pd
from flask import Flask, request, render_template_string
from fuzzywuzzy import fuzz

app = Flask(__name__)

# Function to find similar titles
def find_similar_titles(user_input, df):
    title_choices = df['title'].tolist()
    similar_titles = [title for title in title_choices if fuzz.partial_ratio(user_input, title) >= 80]
    return similar_titles

@app.route('/', methods=['GET', 'POST'])
def index():
    search_form = """
    <form method="POST">
        <label for="filter_value">Enter a title:</label>
        <input type="text" name="filter_value">
        <input type="submit" value="Search">
    </form>
    """

    if request.method == 'POST':
        filter_value = request.form['filter_value'].lower()
        jd['title'] = jd['title'].str.lower()
        filtered_df = jd[jd['title'] == filter_value]

        if not filtered_df.empty:
            details_output = "<h1>Episode Details:</h1>"
            details_df = filtered_df.iloc[:1].drop(['role', 'name', 'summary'], axis=1)
            details_output += details_df.to_html(index=False)

            summary_output = "<h1>Episode Summary:</h1>"
            summary_text = filtered_df['summary'].head(1).values[0]
            summary_output += f"<p>{summary_text}</p>"

            cast_output = "<h1>The Cast:</h1>"
            cast_output += filtered_df[['role', 'name']].to_html(index=False)

            combined_output = search_form + details_output + summary_output + cast_output
        else:
            similar_titles = find_similar_titles(filter_value, jd)

            if similar_titles:
                unique_similar_titles = set()  # Use a set to store unique titles

                similar_titles_list = "<p>Similar titles:</p><ul>"

                for title in similar_titles:
                    # Check if the title is not already in the set
                    if title not in unique_similar_titles:
                        unique_similar_titles.add(title)
                        # Add links that will trigger a new search
                        similar_titles_list += f"<li><a href='?filter_value={title}'>{title}</a></li>"

                similar_titles_list += "</ul>"
                combined_output = search_form + f"No exact match found for '{filter_value}'. {similar_titles_list}"
            else:
                combined_output = search_form + f"No rows found with a title similar to '{filter_value}'"

        return render_template_string(combined_output)

    return search_form

if __name__ == '__main__':
    dwguide = pd.read_csv("dwguide_clean.csv")
    castlist = pd.read_csv("castlist.csv")
    jd = pd.merge(dwguide, castlist, how="left", on="episodenbr")

    app.run(debug=True)
