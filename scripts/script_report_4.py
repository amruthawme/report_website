import pyodbc
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

import config


def generate_mod_report():
    # Define the SQL Server connection string
    server = config.server
    database = config.database
    connection_string = f'Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};Trusted_Connection=yes;'

    # Establish a connection to SQL Server
    connection = pyodbc.connect(connection_string)

    # SQL Query
    sql_query = f"""
        IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'newtable')
        BEGIN
            -- Create a new table if it doesn't exist
            SELECT *
            INTO newtable
            FROM sampletable
            WHERE Change = 'change'
        END
        ELSE
        BEGIN
            -- Update the existing table
            SELECT *
            INTO newtable_temp -- Create a temporary table
            FROM sampletable
            WHERE Change = 'change'
        
            -- Drop the existing table
            DROP TABLE newtable;
        
            -- Rename the temporary table to the original table name
            EXEC sp_rename 'newtable_temp', 'newtable';
        END
    """

    # Print the SQL query for debugging
    print(f"SQL Query: {sql_query}")

    # Execute the SQL query without expecting results
    cursor = connection.cursor()
    cursor.execute(sql_query)

    # Commit the transaction (important for changes to take effect)
    connection.commit()

    # Close the database connection
    connection.close()

# Call the function to generate the report
if __name__ == '__main__':
    generate_mod_report()
