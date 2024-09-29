import PyPDF2
import re
import pandas as pd
import pyodbc
from datetime import datetime
import os


# Function to read PDF and extract table data
def extract_table_data(pdf_file, password):
    with open(pdf_file, "rb") as file:
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


# Function to check if a row exists in the database
def row_exists(cursor, month_year, change_value):
    query = (
        "SELECT COUNT(*) FROM ConsolidateProfit WHERE MonthYear = ? AND ChangeValue = ?"
    )
    cursor.execute(query, (month_year, change_value))
    count = cursor.fetchone()[0]
    return count > 0


# Function to insert data into the database
def insert_into_db(conn, cursor, df):
    for index, row in df.iterrows():
        month_year = row["MonthYear"]
        change_value = row["ChangeValue"]
        if not row_exists(cursor, month_year, change_value):
            cursor.execute(
                "INSERT INTO ConsolidateProfit (MonthYear, ConsolidateValue, ChangeValue, ChangePercentage, CreationDate) VALUES (?, ?, ?, ?, ?)",
                month_year,
                row["ConsolidateValue"],
                change_value,
                row["ChangePercentage"],
                datetime.now(),
            )
            conn.commit()
            print(f"Inserted: {month_year}, {change_value}")
        else:
            print(f"Skipped: {month_year}, {change_value}")


# Database connection parameters
server = "(LocalDB)\\MSSQLLocalDB"
database = "PortfolioTrackerApp"
trusted_connection = "yes"
conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection};MultipleActiveResultSets=true"

# Establish database connection
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Process each PDF file
pdf_folder = "D:/Projects/python-project/docs/NSDL/"
password = ""


for filename in [    
    "AUG_2024",
]:

    pdf_file = f"{pdf_folder}NSDLe-CAS_107508039_{filename}.PDF"
    
    print(pdf_file)
    text = extract_table_data(pdf_file, password)

    # Find the start index of the table
    start_index = text.find("MonthConsolidated Portfolio")
    table_text = text[start_index:]
    # print(table_text)
    # Extract data from the table text using regular expressions
    data = []
    add_rows = True
    lines = table_text.strip().split("\n")[:17]
    for line in lines:
        columns = re.split(r"\s{2,}", line.strip())  # Split by two or more spaces
        # print(columns)
        if columns != [""] and add_rows:
            data.append(columns)
        elif columns == [""] or ["Page 2"]:
            add_rows = False

    # print(data)
    # Initialize lists to store data for each column
    combined_column = []
    change_portfolio = []
    change_rs = []
    change_percent = []

    # Loop through each row in the data
    for row in data[4:]:
        row_data = row[0].split()  # Split the row by spaces
        combined_column.append(
            " ".join(row_data[:2])
        )  # Concatenate Month and Consolidated Portfolio
        change_portfolio.append(row_data[2])
        change_rs.append(row_data[3])
        change_percent.append(row_data[4])

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(
        {
            "MonthYear": combined_column,
            "ConsolidateValue": change_portfolio,
            "ChangeValue": change_rs,
            "ChangePercentage": change_percent,
        }
    )

    # Filter rows where 'Change Rs' is not 'NA'
    df = df[df["ChangeValue"] != "NA"]
    df["ConsolidateValue"] = df["ConsolidateValue"].str.replace(",", "").astype(float)

    # print('===========================')
    print(df)
    # print('=============================')
    # Insert data into the database
    insert_into_db(conn, cursor, df)

# Close database connection
conn.close()
