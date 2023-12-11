# import pyodbc
# import pandas as pd
# import os
# import uuid
#
# # Step 0
# # Define the connection string
# server = 'MPL-SHETTYA'
# database = 'Dummy_test_6'
# driver = '{SQL Server}'
#
# connection_string = f'Driver={{SQL Server Native Client 11.0}};Server={server};Database=master;Trusted_Connection=yes;'
# #connection_string = 'Driver={SQL Server Native Client 11.0};Server=MPL-SHETTYA;Database=master;Trusted_Connection=yes;'
#
#
# # Connect to the SQL Server instance
# connection = pyodbc.connect(connection_string, autocommit=True)
#
# # Create a new database
# cursor = connection.cursor()
# create_database_query = f'CREATE DATABASE {database}'
# cursor.execute(create_database_query)
# connection.commit()
#
# # Close the connection
# #connection.close()
#
# print(f'Database "{database}" created successfully.')
#
# # Step 1
# # Define the path to the folder containing Excel files
# folder_path = 'C:\\Users\\amrutha.shetty\\PycharmProjects\\setup\\venv\\uploads'
#
# # Iterate through all files in the folder
# for file_name in os.listdir(folder_path):
#     # Check if the file is an Excel file
#     if file_name.endswith('.xlsx'):
#         excel_file_path = os.path.join(folder_path, file_name)
#
#         try:
#             # Try to establish a connection
#             cursor = connection.cursor()
#             print("Connection successful.")
#
#             # Read data from Excel into a DataFrame
#             print(excel_file_path)
#             df = pd.read_excel(excel_file_path, sheet_name='Cable')
#
#             # Get the list of column names in your DataFrame
#             columns = df.columns.tolist()
#
#             # Extract the table name from the file name (without extension)
#             #table_name = os.path.splitext(file_name)[0]
#             table_name = 'sampletable'
#             print(table_name)
#
#             # Create an INSERT INTO statement dynamically based on the columns
#             insert_query = f'INSERT INTO {database}.dbo.{table_name} ({", ".join(columns)}) VALUES ({", ".join(["?"] * len(columns))})'
#
#             # Check if the table exists, and create it if it doesn't
#             if not cursor.tables(table=table_name, tableType='TABLE').fetchone():
#                 # Table doesn't exist, so create it
#                 create_table_query = f'CREATE TABLE {database}.dbo.{table_name} ({", ".join([f"{column} NVARCHAR(MAX)" for column in columns])});'
#                 cursor.execute(create_table_query)
#                 connection.commit()
#
#             # Loop through the DataFrame and insert data into SQL Server
#             for index, row in df.iterrows():
#                 # Convert NaN values to None, which is suitable for SQL NULLs
#                 values = [row[column] if not pd.isna(row[column]) else None for column in columns]
#                 cursor.execute(insert_query, values)
#
#             # Define the UPDATE statement to update the existing "ID" column in the table
#             update_query = f'''
#                 UPDATE T
#                 SET T.[ID] = NewID
#                 FROM (
#                     SELECT [ID], ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS NewID
#                     FROM {database}.dbo.{table_name}
#                 ) AS T
#             '''
#
#             # Execute the update query
#             cursor.execute(update_query)
#             connection.commit()
#
#             print(f"Unique IDs added to the 'ID' column in {file_name} successfully.")
#
#
#
#             # # Create an INSERT INTO statement dynamically based on the columns
#             # insert_query = f'INSERT INTO {database}.dbo.{table_name} ({", ".join(columns)}) VALUES ({", ".join(["?"] * len(columns))})'
#
#             # # Check if the table exists, and create it if it doesn't
#             # if not cursor.tables(table=table_name, tableType='TABLE').fetchone():
#             #     # Table doesn't exist, so create it
#             #     create_table_query = f'CREATE TABLE {database}.dbo.{table_name} ({", ".join([f"{column} NVARCHAR(MAX)" for column in columns])});'
#             #     cursor.execute(create_table_query)
#             #     connection.commit()
#             #
#             # # Loop through the DataFrame and insert data into SQL Server
#             # for index, row in df.iterrows():
#             #     # Convert NaN values to None, which is suitable for SQL NULLs
#             #     values = [row[column] if not pd.isna(row[column]) else None for column in columns]
#             #     cursor.execute(insert_query, values)
#
#             # Commit the changes
# #            connection.commit()
#             print(f"Data from {file_name} inserted successfully.")
#
#         except pyodbc.Error as e:
#             # Handle the exception if the connection or insertion fails
#             print(f"Error: {e}")
#
#         finally:
#             # Close the cursor in the 'finally' block to ensure proper cleanup
#             if 'cursor' in locals():
#                 cursor.close()
#
# # Close the connection outside the loop
# if 'connection' in locals():
#     connection.close()
#
#
#
#
#

import sys
import pandas as pd

import pyodbc
import sys
import os
# Add the directory containing config.py to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

import config
import json

print(f"Python Interpreter in Flask App: {sys.executable}")
print(f"pandas version in Flask App: {pd.__version__}")
print(f"pyodbc version in Flask App: {pyodbc.version}")


import os
print(os.path)
import pandas as pd
import pyodbc
import logging

def main():
    # Step 0
    # Define the connection string


    #
    #
    # # Configure logging
    # logging.basicConfig(filename='script.log', level=logging.DEBUG)
    #
    # try:
    #
    #     server = config.server
    #     database = config.database
    #     driver = config.driver
    #
    #     connection_string = f'Driver={{SQL Server Native Client 11.0}};Server={server};Database=master;Trusted_Connection=yes;'
    #
    #     # Connect to the SQL Server instance
    #     connection = pyodbc.connect(connection_string, autocommit=True)
    #
    #     # Create a new database
    #     cursor = connection.cursor()
    #     create_database_query = f'CREATE DATABASE {database}'
    #     cursor.execute(create_database_query)
    #     connection.commit()
    #
    #     print(f'Database "{database}" created successfully.')

    # Configure logging
    logging.basicConfig(filename='logs/script.log', level=logging.DEBUG)

    try:
        server = config.server
        database = config.database
        driver = config.driver
        #folder_path = config.folder_path
        table_name = config.table_name

        connection_string = f'Driver={{SQL Server Native Client 11.0}};Server={server};Database=master;Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string, autocommit=True)
        cursor = connection.cursor()

        # Check if the database already exists
        existing_databases = [row[0] for row in cursor.execute("SELECT name FROM sys.databases")]

        if database in existing_databases:
            # Database exists, so delete it
            delete_query = f'USE master; DROP DATABASE {database};'
            cursor.execute(delete_query)
            connection.commit()

            existing_databases = [row[0] for row in cursor.execute("SELECT name FROM sys.databases")]

        if database not in existing_databases:
            print(f'Database "{database}" successfully deleted.')
        else:
            print(f'Failed to delete database "{database}".')

        # Now create a new database
        cursor.execute(f'CREATE DATABASE {database}')
        connection.commit()
        print(f'New database "{database}" created.')

        # Step 1
        # Define the path to the folder containing Excel files
        folder_path = 'uploads'

        # Iterate through all files in the folder
        for file_name in os.listdir(folder_path):
            # Check if the file is an Excel file
            if file_name.endswith('.xlsx'):
                excel_file_path = os.path.join(folder_path, file_name)

                try:
                    # Try to establish a connection
                    cursor = connection.cursor()
                    print("Connection successful.")

                    # Read data from Excel into a DataFrame
                    print(excel_file_path)
                    df = pd.read_excel(excel_file_path, sheet_name='Cable')

                    desired_cable_tags = df['Cable_Tag'].unique().tolist()
                    cable_dict = {}

                    for desired_cable_tag in desired_cable_tags:
                        df_cable = df[df['Cable_Tag'] == desired_cable_tag]
                        cable_dict[desired_cable_tag] = df_cable.to_dict(orient='list')

                    with open('temp.txt', 'w') as file:
                        json.dump(cable_dict, file)

                    # Get the list of column names in your DataFrame
                    columns = df.columns.tolist()
                    not_interested_columns = ['ID','Status','Length','Cable_Function','Status_Change_Date']
                    columns_upd = list(set(columns) - set(not_interested_columns))
                    column_values = {}
                    # for column in columns_upd:
                    #     column_values[column] = df[column].unique().tolist()
                    # with open('temp.txt', 'w') as file:
                    #     json.dump(column_values, file)


                    # Extract the table name from the file name (without extension)
                    table_name = config.table_name
                    print(table_name)

                    # Create an INSERT INTO statement dynamically based on the columns
                    insert_query = f'INSERT INTO {database}.dbo.{table_name} ({", ".join(columns)}) VALUES ({", ".join(["?"] * len(columns))})'

                    # Check if the table exists, and create it if it doesn't
                    if not cursor.tables(table=table_name, tableType='TABLE').fetchone():
                        # Table doesn't exist, so create it
                        create_table_query = f'CREATE TABLE {database}.dbo.{table_name} ({", ".join([f"{column} NVARCHAR(MAX)" for column in columns])});'
                        cursor.execute(create_table_query)
                        connection.commit()

                    # Loop through the DataFrame and insert data into SQL Server
                    for index, row in df.iterrows():
                        # Convert NaN values to None, which is suitable for SQL NULLs
                        values = [row[column] if not pd.isna(row[column]) else None for column in columns]
                        cursor.execute(insert_query, values)

                    # Define the UPDATE statement to update the existing "ID" column in the table
                    update_query = f'''
                        UPDATE T
                        SET T.[ID] = NewID
                        FROM (
                            SELECT [ID], ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS NewID
                            FROM {database}.dbo.{table_name}
                        ) AS T
                    '''

                    # Execute the update query
                    cursor.execute(update_query)

                    newtable_query = f"""
                    Use {database}
                    CREATE TABLE cab_info (
                        Cabinet_ID varchar(10),
                        Cabinet_Description varchar(25)
                    )
                
                    INSERT INTO cab_info (Cabinet_ID, Cabinet_Description)
                    VALUES
                        ('3510', 'Breaker D2142'),
                        ('3511', 'Breaker 11142'),
                        ('3630', 'Line 1 S1 Relay'),
                        ('3631', 'Line 1 S2 Relay'),
                        ('3632', 'Line 1 Control'),
                        ('3633', 'Line 2 S1 Relay'),
                        ('3634', 'Line 2 S2 Relay'),
                        ('3635', 'Line 3 S1 Relay'),
                        ('3636', 'Line 3 S2 Relay'),
                        ('3637', 'Comm T-1'),
                        ('3638', 'Comm T-2'),
                        ('3639', 'Comm T-3'),
                        ('3640', 'Comm T-4'),
                        ('3641', 'Security Cabinet'),
                        ('3801', 'Yard Interface S1'),
                        ('3802', 'Yard Interface S2'),
                        ('4100', 'DFR'),
                        ('2601', 'SYNC'),
                        ('3901', 'AC3 Distribution'),
                        ('3911', 'DCS1-2 Distribution'),
                        ('3912', 'DCS2-2 Distribution');
                    """
                    cursor.execute(newtable_query)

                    connection.commit()

                    print(f"Unique IDs added to the 'ID' column in {file_name} successfully.")


                except pyodbc.Error as e:
                    # Handle the exception if the connection or insertion fails
                    print(f"Error: {e}")

                finally:
                    # Close the cursor in the 'finally' block to ensure proper cleanup
                    if 'cursor' in locals():
                        cursor.close()

        # Close the connection outside the loop
        if 'connection' in locals():
            connection.close()

    except Exception as e:
        # Log any exceptions
        logging.error(f'Error in script.py: {str(e)}')





if __name__ == '__main__':
    main()
