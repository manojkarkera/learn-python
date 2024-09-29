import pyodbc
from datetime import datetime

 # Define connection parameters
server = '(LocalDB)\\MSSQLLocalDB'
database = 'PortfolioTrackerApp'
trusted_connection = 'yes'  # True in .NET becomes 'yes' in pyodbc

# Create connection string
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection};MultipleActiveResultSets=true'

# Establish connection
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Check if row already exists in the database
def row_exists(month_year):
    print(f'{month_year}')
    query = "SELECT COUNT(*) FROM ConsolidateProfit WHERE MonthYear = ?"
    cursor.execute(query, (month_year,))
    count = cursor.fetchone()[0]
    print(f'Total {count}')
    return count > 0

def insert_into_db(df):

    # Insert DataFrame into the newly created table
    for index, row in df.iterrows():
        month_year = row['MonthYear']
        if not row_exists(month_year):
            cursor.execute("INSERT INTO ConsolidateProfit (MonthYear, ConsolidateValue, ChangeValue, ChangePercentage, CreationDate) VALUES (?, ?, ?, ?, ?)",
                        month_year, row['ConsolidateValue'], row['ChangeValue'], row['ChangePercentage'], datetime.now())
            conn.commit()
            test = 1
        else:
            print(f"Row with Month_Year '{month_year}' already exists. Skipping insertion.")

    # Close connection
    conn.close()

    print("Data inserted successfully!")
