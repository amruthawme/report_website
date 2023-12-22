import pyodbc
import os
import sys
import logging
from datetime import datetime
from config import server, database, driver, table_name
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def update_database(cableTag, change,notes, color1, wireLabel1, otb1, opoint1, dtb1, dpoint1,
                    color2, wireLabel2, otb2, opoint2, dtb2, dpoint2,
                    color3, wireLabel3, otb3, opoint3, dtb3, dpoint3,
                    color4, wireLabel4, otb4, opoint4, dtb4, dpoint4,
                    color5, wireLabel5, otb5, opoint5, dtb5, dpoint5,
                    color6, wireLabel6, otb6, opoint6, dtb6, dpoint6,
                    color7, wireLabel7, otb7, opoint7, dtb7, dpoint7):

    logging.basicConfig(filename='logs/upd_script.log', level=logging.DEBUG)
    #logging.basicConfig(filename='logs/upd_script.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    try:
        # Read configuration from config.py file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(script_dir, 'config.py')
        with open(config_file_path) as config_file:
            config_code = compile(config_file.read(), config_file_path, 'exec')
            config_globals = {}
            exec(config_code, config_globals)

        server = config_globals.get('server')
        database = config_globals.get('database')
        driver = config_globals.get('driver')
        table_name = config_globals.get('table_name')


        connection_string = f'Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string, autocommit=True)
        cursor = connection.cursor()

        # Replace None values with an empty string
        params = [
            change,
            notes,
            *[value if value is not None else '' for value in (
                color1, wireLabel1, otb1, opoint1, dtb1, dpoint1,
                color2, wireLabel2, otb2, opoint2, dtb2, dpoint2,
                color3, wireLabel3, otb3, opoint3, dtb3, dpoint3,
                color4, wireLabel4, otb4, opoint4, dtb4, dpoint4,
                color5, wireLabel5, otb5, opoint5, dtb5, dpoint5,
                color6, wireLabel6, otb6, opoint6, dtb6, dpoint6,
                color7, wireLabel7, otb7, opoint7, dtb7, dpoint7,
            )],
            cableTag
        ]

        # Construct your SQL UPDATE query based on the form data
        update_query = f'''
            UPDATE {database}.dbo.{table_name}
            SET Change = ?,
                Change_Notes = ?,
                Color1 = ?,
                Wire_Label1 = ?,
                OTB1 = ?,
                OPoint1 = ?,
                DTB1 = ?,
                DPoint1 = ?,
                Color2 = ?,
                Wire_Label2 = ?,
                OTB2 = ?,
                OPoint2 = ?,
                DTB2 = ?,
                DPoint2 = ?,
                Color3 = ?,
                Wire_Label3 = ?,
                OTB3 = ?,
                OPoint3 = ?,
                DTB3 = ?,
                DPoint3 = ?,
                Color4 = ?,
                Wire_Label4 = ?,
                OTB4 = ?,
                OPoint4 = ?,
                DTB4 = ?,
                DPoint4 = ?,
                Color5 = ?,
                Wire_Label5 = ?,
                OTB5 = ?,
                OPoint5 = ?,
                DTB5 = ?,
                DPoint5 = ?,
                Color6 = ?,
                Wire_Label6 = ?,
                OTB6 = ?,
                OPoint6 = ?,
                DTB6 = ?,
                DPoint6 = ?,
                Color7 = ?,
                Wire_Label7 = ?,
                OTB7 = ?,
                OPoint7 = ?,
                DTB7 = ?,
                DPoint7 = ?
            WHERE Cable_Tag = ?
        '''

        # Print the SQL query and parameters for debugging
        print(f"Executing SQL Query: {update_query}")
        print(f"Parameters: {params}")

        # Execute the SQL query with the form data
        cursor.execute(update_query, *params)
        logging.info(f'Executing SQL Query: {update_query}{current_time}')
        logging.info(f'Parameters: {params}{current_time}')
        logging.info(f"Rows affected: {cursor.rowcount}{current_time}")
        connection.commit()

        return 'Database Updated Successfully'

    except pyodbc.Error as e:
        return f'Error updating database: {str(e)}'

    finally:
        if 'connection' in locals():
            connection.close()

