import config
import os
print(os.path)
import pyodbc



def main():
    # Step 0
    # Define the connection string

    import logging

    # Configure logging
    logging.basicConfig(filename='logs/script.log', level=logging.DEBUG)

    try:

        server = config.server

        connection_string = f'Driver={{SQL Server Native Client 11.0}};Server={server};Database=master;Trusted_Connection=yes;'

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
