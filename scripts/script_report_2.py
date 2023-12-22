import os
import pandas as pd
import pyodbc
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

import config


def generate_report():
    # Define the SQL Server connection string
    server = config.server
    database = config.database
    connection_string = f'Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};Trusted_Connection=yes;'

    # Establish a connection to SQL Server`
    connection = pyodbc.connect(connection_string)

    # SQL Query
    sql_query = """
        SELECT DISTINCT *
    FROM (
    SELECT DISTINCT ID, Cable_Tag, Cabinet_Origination AS Origination, OTB1 AS OTB, Cabinet_Destination AS Destination, DTB1 AS DTB, Awg_Cond
    FROM sampletable
    WHERE OTB1 IS NOT NULL AND DTB1 IS NOT NULL
    UNION ALL
    SELECT DISTINCT ID, Cable_Tag, Cabinet_Origination AS Origination, OTB2 AS OTB, Cabinet_Destination AS Destination, DTB2 AS DTB, Awg_Cond
    FROM sampletable
    WHERE OTB2 IS NOT NULL AND DTB2 IS NOT NULL
    UNION ALL
    SELECT DISTINCT ID, Cable_Tag, Cabinet_Origination AS Origination, OTB3 AS OTB, Cabinet_Destination AS Destination, DTB3 AS DTB, Awg_Cond
    FROM sampletable
    WHERE OTB3 IS NOT NULL AND DTB3 IS NOT NULL
    UNION ALL
    SELECT DISTINCT ID, Cable_Tag, Cabinet_Origination AS Origination, OTB4 AS OTB, Cabinet_Destination AS Destination, DTB4 AS DTB, Awg_Cond
    FROM sampletable
    WHERE OTB4 IS NOT NULL AND DTB4 IS NOT NULL
    UNION ALL
    SELECT DISTINCT ID, Cable_Tag, Cabinet_Origination AS Origination, OTB5 AS OTB, Cabinet_Destination AS Destination, DTB5 AS DTB, Awg_Cond
    FROM sampletable
    WHERE OTB5 IS NOT NULL AND DTB5 IS NOT NULL
    UNION ALL
    SELECT DISTINCT ID, Cable_Tag, Cabinet_Origination AS Origination, OTB6 AS OTB, Cabinet_Destination AS Destination, DTB6 AS DTB, Awg_Cond
    FROM sampletable
    WHERE OTB6 IS NOT NULL AND DTB6 IS NOT NULL
    UNION ALL
    SELECT DISTINCT ID, Cable_Tag, Cabinet_Origination AS Origination, OTB7 AS OTB, Cabinet_Destination AS Destination, DTB7 AS DTB, Awg_Cond
    FROM sampletable
    WHERE OTB7 IS NOT NULL AND DTB7 IS NOT NULL
    )AS subquery;
    """

    # Execute the SQL query and read the results into a DataFrame
    df = pd.read_sql(sql_query, connection)

    # Close the database connection
    connection.close()

    # Define the directory where reports will be saved
    reports_directory = 'reports'

    # Ensure the reports directory exists
    if not os.path.exists(reports_directory):
        os.makedirs(reports_directory)

    # Define the report file name
    report_name = config.report2_name

    # Construct the full path to save the Excel file
    excel_file_path = os.path.join(reports_directory, report_name)

    # Save the DataFrame to an Excel file
    df.to_excel(excel_file_path, index=False)

    print(f'Data saved to {excel_file_path}')

# Call the function to generate the report
if __name__ == '__main__':
    generate_report()