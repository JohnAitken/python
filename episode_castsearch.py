import pandas as pd
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        filter_value = request.form['filter_value'].lower()
        jd['title'] = jd['title'].str.lower()
        filtered_df = jd[jd['title'] == filter_value]

        if not filtered_df.empty:
            details_output = "<h1>Episode Details:</h1>"
            details_df = filtered_df.iloc[:1].drop(['role', 'name', 'summary'], axis=1)
            details_output += details_df.to_html(index=False)

            summary_output = "<h1>Episode Summary:</h1>"
            summary_output += filtered_df['summary'].head(1).to_string(index=False)

            cast_output = "<h1>The Cast:</h1>"
            cast_output += filtered_df[['role', 'name']].to_html(index=False)

            combined_output = details_output + summary_output + cast_output
        else:
            combined_output = f"No rows found with title equal to {filter_value}"

        return render_template_string(combined_output)

    return """
    <form method="POST">
        <label for="filter_value">Enter the value to filter by:</label>
        <input type="text" name="filter_value">
        <input type="submit" value="Search">
    </form>
    """

if __name__ == '__main__':
    dwguide = pd.read_csv("dwguide_clean.csv")
    castlist = pd.read_csv("castlist.csv")
    jd = pd.merge(dwguide, castlist, how="left", on="episodenbr")
    
    app.run(debug=True)
