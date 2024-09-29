import PyPDF2
import tabula
import re
import pandas as pd
from insert_data import insert_into_db  # Import function from the insertion script

def read_pdf(file_path, password):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file, strict=False)
        if pdf_reader.is_encrypted:
            # Try to decrypt the PDF with the provided password
            if pdf_reader.decrypt(password):
                num_pages = len(pdf_reader.pages)
                text = ""
                for page_number in range(num_pages):
                    text += pdf_reader.pages[page_number].extract_text()
                return text
            else:
                raise ValueError("Incorrect password")
        else:
            # PDF is not encrypted, so just read and extract text
            num_pages = len(pdf_reader.pages)
            text = ""
            for page_number in range(num_pages):
                text += pdf_reader.pages[page_number].extract_text()
            return text

# Example usage:
pdf_file = "D:/Projects/python-project/docs/NSDLe-CAS_107508039_APR_2024.PDF"  # Replace with the path to your PDF file
password = "AOSPM2900F"  # Replace with the actual password
text = read_pdf(pdf_file, password)
# tables = tabula.read_pdf(pdf_file, pages="all", multiple_tables=True, password=password)

# print(tables)
print("Text extracted from PDF:")
# print(text)

# Find the start index of the table (where the word "Month" is found)
start_index = text.find("MonthConsolidated Portfolio")

# print(start_index)

# Extract the table text from the start index to the end of the text
table_text = text[start_index:]

# Extract data from the table text using regular expressions
data = []
add_rows = True  # Flag variable to control row addition

for line in table_text.strip().split("\n"):
    columns = re.split(r"\s{2,}", line.strip())  # Split by two or more spaces
    if columns != [''] and add_rows:  # Check if all columns are not empty and rows can still be added
        data.append(columns)
    elif columns == ['']:  # If all columns are empty, stop adding rows
        add_rows = False

print(data)

# Initialize lists to store data for each column
combined_column = []
change_portfolio = []
change_rs = []
change_percent = []

# Loop through each row in the data
for row in data[4:]:
    row_data = row[0].split()  # Split the row by spaces
    # Concatenate Month and Consolidated Portfolio into one column
    combined_column.append(' '.join(row_data[:2]))
    # Append remaining elements to respective columns
    change_portfolio.append(row_data[2])
    change_rs.append(row_data[3])
    change_percent.append(row_data[4])

# Create a DataFrame from the extracted data
df = pd.DataFrame({
    'MonthYear': combined_column,
    'ConsolidateValue': change_portfolio,
    'ChangeValue': change_rs,
    'ChangePercentage': change_percent
})

# Filter rows where 'Change Rs' is not 'NA'
df = df[df['ChangeValue'] != 'NA']
df['ConsolidateValue'] = df['ConsolidateValue'].str.replace(',', '').astype(float)

# Print the DataFrame
print("DataFrame:")
print(df)

insert_into_db(df)

# for column in df.columns:
#     print(column, df[column].values)