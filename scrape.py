import fitz  # PyMuPDF
import os
import pandas as pd
from datetime import datetime

# Set the working directory
os.chdir("C:/Users/JA/Documents/Git_Repositories/R/pdfScrapeDev")


# Function to perform OCR on a PDF file
def ocr_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    return text


# PDF file
pdf_file = "10088075_10055_202324.pdf"

# Perform OCR on the PDF file
text = ocr_pdf(pdf_file)

# Number of pages
num_pages = 4

# Initialize a list to store results
all_results = []

# Loop through pages 2 to num_pages+1
for page_num in range(2, num_pages + 2):
    text_lines = text.split("\n")
    # Create a DataFrame with index, page, text_lines, and pdf_file columns
    result_df = pd.DataFrame(
        {
            "index": range(1, len(text_lines) + 1),
            "page": [page_num - 1] * len(text_lines),
            "text_lines": text_lines,
            "pdf_file": [pdf_file] * len(text_lines),
        }
    )
    all_results.append(result_df)

# Combine the results into a single DataFrame
df = pd.concat(all_results, ignore_index=True)

# Calculate and print the elapsed time
end_time = datetime.now()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time.total_seconds(), "seconds")
