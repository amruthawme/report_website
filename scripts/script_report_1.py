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
    connection_string = f'Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};Trusted_Connection=yes;'

    # Establish a connection to SQL Server
    connection = pyodbc.connect(connection_string)

    # SQL Query
    sql_query = """
    SELECT Cabinet_Origination as Origination, Wire_Label1 AS Wire_label, Color1 AS Color, OTB1 AS OTB, OPoint1 as OPNT, Cabinet_Destination as Destination,DTB1 as DTB,DPoint1 as DPNT, ID, Cable_Tag, System
    FROM sampletable
    UNION ALL
    SELECT Cabinet_Origination as Origination, Wire_Label2 AS Wire_label, Color2 AS Color, OTB2 AS OTB, OPoint2 as OPNT, Cabinet_Destination as Destination,DTB2 as DTB,DPoint2 as DPNT, ID, Cable_Tag, System
    FROM sampletable
    UNION ALL
    SELECT Cabinet_Origination as Origination, Wire_Label3 AS Wire_label, Color3 AS Color, OTB3 AS OTB, OPoint3 as OPNT, Cabinet_Destination as Destination,DTB3 as DTB,DPoint3 as DPNT, ID, Cable_Tag, System
    FROM sampletable
    UNION ALL
    SELECT Cabinet_Origination as Origination, Wire_Label4 AS Wire_label, Color4 AS Color, OTB4 AS OTB, OPoint4 as OPNT, Cabinet_Destination as Destination,DTB4 as DTB,DPoint4 as DPNT, ID, Cable_Tag, System
    FROM sampletable
    UNION ALL
    SELECT Cabinet_Origination as Origination, Wire_Label5 AS Wire_label, Color5 AS Color, OTB5 AS OTB, OPoint5 as OPNT, Cabinet_Destination as Destination,DTB5 as DTB,DPoint5 as DPNT, ID, Cable_Tag, System
    FROM sampletable
    UNION ALL
    SELECT Cabinet_Origination as Origination, Wire_Label6 AS Wire_label, Color6 AS Color, OTB6 AS OTB, OPoint6 as OPNT, Cabinet_Destination as Destination,DTB6 as DTB,DPoint6 as DPNT, ID, Cable_Tag, System
    FROM sampletable
    UNION ALL
    SELECT Cabinet_Origination as Origination, Wire_Label7 AS Wire_label, Color7 AS Color, OTB7 AS OTB, OPoint7 as OPNT, Cabinet_Destination as Destination,DTB7 as DTB,DPoint7 as DPNT, ID, Cable_Tag, System
    FROM sampletable
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
    report_name = config.report1_name

    # Construct the full path to save the Excel file
    excel_file_path = os.path.join(reports_directory, report_name)

    # Save the DataFrame to an Excel file
    df.to_excel(excel_file_path, index=False)

    print(f'Data saved to {excel_file_path}')

# Call the function to generate the report
if __name__ == '__main__':
    generate_report()