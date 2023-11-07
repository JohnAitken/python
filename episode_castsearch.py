import pandas as pd
from flask import Flask, request, render_template_string, redirect, url_for
from fuzzywuzzy import fuzz

app = Flask(__name__)

# Function to find similar titles
def find_similar_titles(user_input, df):
    title_choices = df['title'].tolist()
    similar_titles = [title for title in title_choices if fuzz.partial_ratio(user_input, title) >= 80]
    return set(similar_titles)  # Use a set to store unique titles

@app.route('/', methods=['GET', 'POST'])
def index():
    search_form = """
    <form method="POST">
        <label for="filter_value">Enter a title:</label>
        <input type="text" name="filter_value" id="filter_value">
        <input type="submit" value="Search">
    </form>
    """

    script = """
    <script>
        function setFilterValueAndSubmit(value) {
            document.getElementById('filter_value').value = value;
        }
    </script>
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
                similar_titles_list = "<p>Similar titles:</p><ul>"
                for title in similar_titles:
                    similar_titles_list += f"<li><a href='#' onclick='setFilterValueAndSubmit(\"{title}\")'>{title}</a></li>"
                similar_titles_list += "</ul>"
                combined_output = search_form + f"No exact match found for '{filter_value}'. {similar_titles_list}"
            else:
                combined_output = search_form + f"No rows found with a title similar to '{filter_value}'"

        return render_template_string(combined_output + script)

    return search_form + script

if __name__ == '__main__':
    dwguide = pd.read_csv("dwguide_clean.csv")
    castlist = pd.read_csv("castlist.csv")
    jd = pd.merge(dwguide, castlist, how="left", on="episodenbr")

    app.run(debug=True)


# This code is a Python script that uses the Flask web framework and the FuzzyWuzzy library to create a simple web application for searching and displaying information about episodes of a TV show. Here's a detailed explanation of the code:

#     Importing libraries and modules:
#         import pandas as pd: This imports the Pandas library and gives it the alias 'pd,' which is commonly used to work with data in tabular form.
#         from flask import Flask, request, render_template_string, redirect, url_for: This imports various functions and classes from the Flask library, including Flask (the web application framework), request (for handling HTTP requests), render_template_string (for rendering HTML templates), and others.
#         from fuzzywuzzy import fuzz: This imports the fuzz function from the FuzzyWuzzy library, which is used for fuzzy string matching.

#     Creating a Flask application:
#         app = Flask(__name__): This initializes a Flask web application. The __name__ variable is set to the name of the current module, which is used to determine the root path for the application.

#     Defining a function to find similar titles:
#         find_similar_titles(user_input, df): This is a custom function that takes user input (a string) and a Pandas DataFrame df as input. It uses FuzzyWuzzy's fuzz.partial_ratio function to find titles in the DataFrame that are similar to the user input. It returns a set of similar titles to ensure uniqueness.

#     Creating a route for the root URL ("/"):
#         @app.route('/', methods=['GET', 'POST']): This is a Flask route decorator that defines the behavior for both GET and POST requests to the root URL ("/").

#     The index function:
#         This function handles requests to the root URL ("/"). It performs the following tasks:
#             Defines an HTML form for user input to search for episode titles.
#             Checks if the request method is POST (i.e., a form submission).
#             If the request method is POST:
#                 Retrieves the user's input from the submitted form.
#                 Converts the titles in the DataFrame jd to lowercase and filters it based on the user's input.
#                 If an exact match is found, it displays episode details, summary, and cast information.
#                 If no exact match is found, it searches for similar titles using the find_similar_titles function and provides a list of similar titles.
#             If the request method is GET (i.e., a regular page load), it displays the search form.

#     HTML templates and JavaScript:
#         The code includes HTML and JavaScript code to define the structure of the web page. It provides a search form, displays episode details, summary, and cast information, and also allows users to click on similar titles for a new search.

#     Reading and merging data:
#         The code reads two CSV files, "dwguide_clean.csv" and "castlist.csv," into Pandas DataFrames (dwguide and castlist). These DataFrames are then merged based on a common column ("episodenbr") using the pd.merge function, creating a new DataFrame jd that contains information about episodes and their cast.

#     Running the Flask application:
#         The code checks if it's the main module and then runs the Flask application in debug mode.

# When the Flask application is run, it serves as a web interface for searching and displaying information about episodes of the TV show, and it provides suggestions for similar titles if there's no exact match. The application's behavior is defined by the index function, and the HTML structure is defined within the code.