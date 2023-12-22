# import config
import os
print(os.path)
import pyodbc
import sys
import os


# Add the parent directory of the script to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)
# Print sys.path for debugging
# print(sys.path)

# Now import config
import config

def main():
    # Step 0
    # Define the connection string

    import logging

    # Configure logging
    logging.basicConfig(filename='logs/script.log', level=logging.DEBUG)
    # logging.basicConfig(filename=log_file_path, level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

    try:

        server = config.server

        connection_string = f'Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database=master;Trusted_Connection=yes;'

        # Connect to the SQL Server instance
        connection = pyodbc.connect(connection_string, autocommit=True)

        # Create a new database
        cursor = connection.cursor()
        dbnames_query = f"""
                    SELECT name FROM sys.databases
                    """
        dbnames = cursor.execute(dbnames_query)
        database_names = [row[0] for row in dbnames]
        print(database_names)
        connection.commit()

    except pyodbc.Error as e:
        # Handle the exception if the connection or insertion fails
        print(f"Error: {e}")

    finally:
        # Close the cursor in the 'finally' block to ensure proper cleanup
        if 'cursor' in locals():
            cursor.close()




if __name__ == '__main__':
    main()
