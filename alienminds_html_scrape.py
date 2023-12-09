import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "http://alienminds.blogspot.com/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract the text content of the webpage
text_content = soup.get_text()

# Split the text content into lines
lines = text_content.split("\n")

# Remove blank lines
lines = [line for line in lines if line.strip() != ""]

# Join the lines back together
text_content = "\n".join(lines)

# Write the text content to a Markdown file
with open("webpage_content.md", "w", encoding="utf-8") as f:
    f.write(text_content)

print("The text content has been written to 'webpage_content.md'")
