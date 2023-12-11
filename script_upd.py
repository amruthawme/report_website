import pyodbc
import os
import sys
# script_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(script_dir)
# sys.path.append(parent_dir)
#
# import config
import logging

from config import server, database, driver, table_name

# def update_database(cableTag, change, notes, color1, wireLabel1, otb1, ...):
# def update_database(cableTag, change, color1, wireLabel1, otb1,opoint1,dtb1,dpoint1,
#                     color2, wireLabel2, otb2,opoint2,dtb2,dpoint2,
#                     color3, wireLabel3, otb3,opoint3,dtb3,dpoint3,
#                     color4, wireLabel4, otb4,opoint4,dtb4,dpoint4,
#                     color5, wireLabel5, otb5,opoint5,dtb5,dpoint5,
#                     color6, wireLabel6, otb6,opoint6,dtb6,dpoint6,
#                     color7, wireLabel7, otb7,opoint7,dtb7,dpoint7,
#                     ):
#     logging.basicConfig(filename='upd_script.log', level=logging.DEBUG)
#
#     try:
#         server = config.server
#         database = config.database
#         driver = config.driver
#         #folder_path = config.folder_path
#         table_name = config.table_name
#
#         connection_string = f'Driver={{SQL Server Native Client 11.0}};Server={server};Database=master;Trusted_Connection=yes;'
#         connection = pyodbc.connect(connection_string, autocommit=True)
#         cursor = connection.cursor()
#
#         # Construct your SQL UPDATE query based on the form data
#         update_query = f'''
#             UPDATE {database}.dbo.{table_name}
#             SET Change = ?,
#                 Color1 = COALESCE(?, NULL),
#                 Wire_Label1 = COALESCE(?, NULL),
#                 OTB1 = COALESCE(?, NULL),
#                 OPoint1 = COALESCE(?, NULL),
#                 DTB1 = COALESCE(?, NULL),
#                 DPoint1 = COALESCE(?, NULL),
#                 Color2 = COALESCE(?, NULL),
#                 Wire_Label2 = COALESCE(?, NULL),
#                 OTB2 = COALESCE(?, NULL),
#                 OPoint2 = COALESCE(?, NULL),
#                 DTB2 = COALESCE(?, NULL),
#                 DPoint2 = COALESCE(?, NULL),
#                 Color3 = COALESCE(?, NULL),
#                 Wire_Label3 = COALESCE(?, NULL),
#                 OTB3 = COALESCE(?, NULL),
#                 OPoint3 = COALESCE(?, NULL),
#                 DTB3 = COALESCE(?, NULL),
#                 DPoint3 = COALESCE(?, NULL),
#                 Color4 = COALESCE(?, NULL),
#                 Wire_Label4 = COALESCE(?, NULL),
#                 OTB4 = COALESCE(?, NULL),
#                 OPoint4 = COALESCE(?, NULL),
#                 DTB4 = COALESCE(?, NULL),
#                 DPoint4 = COALESCE(?, NULL),
#                 Color5 = COALESCE(?, NULL),
#                 Wire_Label5 = COALESCE(?, NULL),
#                 OTB5 = COALESCE(?, NULL),
#                 OPoint5 = COALESCE(?, NULL),
#                 DTB5 = COALESCE(?, NULL),
#                 DPoint5 = COALESCE(?, NULL),
#                 Color6 = COALESCE(?, NULL),
#                 Wire_Label6 = COALESCE(?, NULL),
#                 OTB6 = COALESCE(?, NULL),
#                 OPoint6 = COALESCE(?, NULL),
#                 DTB6 = COALESCE(?, NULL),
#                 DPoint6 = COALESCE(?, NULL),
#                 Color7 = COALESCE(?, NULL),
#                 Wire_Label7 = COALESCE(?, NULL),
#                 OTB7 = COALESCE(?, NULL),
#                 OPoint7 = COALESCE(?, NULL),
#                 DTB7 = COALESCE(?, NULL),
#                 DPoint7 = COALESCE(?, NULL)
#             WHERE Cable_Tag = ?
#         '''
#
#         # Execute the SQL query with the form data
#         # Replace None with a default value (e.g., an empty string) using a list comprehension
#         # Replace None with a default value (e.g., an empty string) and "nan" with a suitable default
#         # Replace None with a default value (e.g., an empty string) and "nan" with a suitable default
#         default_value = ''
#
#         # Build the params list manually
#         params = [
#             change,
#             color1, wireLabel1, otb1, opoint1, dtb1, dpoint1,
#             color2, wireLabel2, otb2, opoint2, dtb2, dpoint2,
#             color3, wireLabel3, otb3, opoint3, dtb3, dpoint3,
#             color4, wireLabel4, otb4, opoint4, dtb4, dpoint4,
#             color5, wireLabel5, otb5, opoint5, dtb5, dpoint5,
#             color6, wireLabel6, otb6, opoint6, dtb6, dpoint6,
#             color7, wireLabel7, otb7, opoint7, dtb7, dpoint7,
#             cableTag
#         ]
#
#         # # Replace "nan" and None values with the default value
#         # for i in range(len(params)):
#         #     if params[i] is None or str(params[i]).lower() == 'nan':
#         #         params[i] = default_value
#
#
#
#         logging.info(f'Executing SQL Query: {update_query}')
#         logging.info(f'Parameters: {params}')
#
#         cursor.execute(update_query, *params)
#         logging.info(f"Rows affected: {cursor.rowcount}")
#         connection.commit()
#
#         return 'Database Updated Successfully'
#
#     except pyodbc.Error as e:
#         return f'Error updating database: {str(e)}'
#
#     finally:
#         if 'connection' in locals():
#             connection.close()


# def update_database(cableTag, change, color1, wireLabel1, otb1, opoint1, dtb1, dpoint1,
#                     color2, wireLabel2, otb2, opoint2, dtb2, dpoint2,
#                     color3, wireLabel3, otb3, opoint3, dtb3, dpoint3,
#                     color4, wireLabel4, otb4, opoint4, dtb4, dpoint4,
#                     color5, wireLabel5, otb5, opoint5, dtb5, dpoint5,
#                     color6, wireLabel6, otb6, opoint6, dtb6, dpoint6,
#                     color7, wireLabel7, otb7, opoint7, dtb7, dpoint7):
#
#     logging.basicConfig(filename='upd_script.log', level=logging.DEBUG)
#
#     try:
#         server = config.server
#         database = config.database
#         driver = config.driver
#         table_name = config.table_name
#
#         connection_string = f'Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};Trusted_Connection=yes;'
#         connection = pyodbc.connect(connection_string, autocommit=True)
#         cursor = connection.cursor()
#
#         # Replace None values with an empty string
#         params = [
#             change,
#             *[value if value is not None else '' for value in (
#                 color1, wireLabel1, otb1, opoint1, dtb1, dpoint1,
#                 color2, wireLabel2, otb2, opoint2, dtb2, dpoint2,
#                 color3, wireLabel3, otb3, opoint3, dtb3, dpoint3,
#                 color4, wireLabel4, otb4, opoint4, dtb4, dpoint4,
#                 color5, wireLabel5, otb5, opoint5, dtb5, dpoint5,
#                 color6, wireLabel6, otb6, opoint6, dtb6, dpoint6,
#                 color7, wireLabel7, otb7, opoint7, dtb7, dpoint7,
#             )],
#             cableTag
#         ]
#
#         # Construct your SQL UPDATE query based on the form data
#         update_query = f'''
#             UPDATE {database}.dbo.{table_name}
#             SET Change = ?,
#                 Color1 = ?,
#                 Wire_Label1 = ?,
#                 OTB1 = ?,
#                 OPoint1 = ?,
#                 DTB1 = ?,
#                 DPoint1 = ?,
#                 Color2 = ?,
#                 Wire_Label2 = ?,
#                 OTB2 = ?,
#                 OPoint2 = ?,
#                 DTB2 = ?,
#                 DPoint2 = ?,
#                 Color3 = ?,
#                 Wire_Label3 = ?,
#                 OTB3 = ?,
#                 OPoint3 = ?,
#                 DTB3 = ?,
#                 DPoint3 = ?,
#                 Color4 = ?,
#                 Wire_Label4 = ?,
#                 OTB4 = ?,
#                 OPoint4 = ?,
#                 DTB4 = ?,
#                 DPoint4 = ?,
#                 Color5 = ?,
#                 Wire_Label5 = ?,
#                 OTB5 = ?,
#                 OPoint5 = ?,
#                 DTB5 = ?,
#                 DPoint5 = ?,
#                 Color6 = ?,
#                 Wire_Label6 = ?,
#                 OTB6 = ?,
#                 OPoint6 = ?,
#                 DTB6 = ?,
#                 DPoint6 = ?,
#                 Color7 = ?,
#                 Wire_Label7 = ?,
#                 OTB7 = ?,
#                 OPoint7 = ?,
#                 DTB7 = ?,
#                 DPoint7 = ?
#             WHERE Cable_Tag = ?
#         '''
#
#         # Execute the SQL query with the form data
#         cursor.execute(update_query, *params)
#         logging.info(f"Rows affected: {cursor.rowcount}")
#         connection.commit()
#
#         return 'Database Updated Successfully'
#
#     except pyodbc.Error as e:
#         return f'Error updating database: {str(e)}'
#
#     finally:
#         if 'connection' in locals():
#             connection.close()


def update_database(cableTag, change,notes, color1, wireLabel1, otb1, opoint1, dtb1, dpoint1,
                    color2, wireLabel2, otb2, opoint2, dtb2, dpoint2,
                    color3, wireLabel3, otb3, opoint3, dtb3, dpoint3,
                    color4, wireLabel4, otb4, opoint4, dtb4, dpoint4,
                    color5, wireLabel5, otb5, opoint5, dtb5, dpoint5,
                    color6, wireLabel6, otb6, opoint6, dtb6, dpoint6,
                    color7, wireLabel7, otb7, opoint7, dtb7, dpoint7):

    logging.basicConfig(filename='logs/upd_script.log', level=logging.DEBUG)

    # try:
    #     server = config.server
    #     database = config.database
    #     driver = config.driver
    #     table_name = config.table_name
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


        connection_string = f'Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};Trusted_Connection=yes;'
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
        logging.info(f'Executing SQL Query: {update_query}')
        logging.info(f'Parameters: {params}')
        logging.info(f"Rows affected: {cursor.rowcount}")
        connection.commit()

        return 'Database Updated Successfully'

    except pyodbc.Error as e:
        return f'Error updating database: {str(e)}'

    finally:
        if 'connection' in locals():
            connection.close()

# # Call the function with sample data
# update_result = update_database(
#     cableTag='your_cable_tag',
#     change='change_value',
#     color1='color1_value',
#     wireLabel1='wire_label1_value',
#     otb1='otb1_value',
#     opoint1='opoint1_value',
#     dtb1='dtb1_value',
#     dpoint1='dpoint1_value',
#     color2='color1_value',
#     wireLabel2='wire_label1_value',
#     otb2='otb1_value',
#     opoint2='opoint1_value',
#     dtb2='dtb1_value',
#     dpoint2='dpoint1_value',
#     color3='color1_value',
#     wireLabel3='wire_label1_value',
#     otb3='otb1_value',
#     opoint3='opoint1_value',
#     dtb3='dtb1_value',
#     dpoint3='dpoint1_value',
#     color4='color1_value',
#     wireLabel4='wire_label1_value',
#     otb4='otb1_value',
#     opoint4='opoint1_value',
#     dtb4='dtb1_value',
#     dpoint4='dpoint1_value',
#     color5='color1_value',
#     wireLabel5='wire_label1_value',
#     otb5='otb1_value',
#     opoint5='opoint1_value',
#     dtb5='dtb1_value',
#     dpoint5='dpoint1_value',
#     color6='color1_value',
#     wireLabel6='wire_label1_value',
#     otb6='otb1_value',
#     opoint6='opoint1_value',
#     dtb6='dtb1_value',
#     dpoint6='dpoint1_value',
#     color7='color1_value',
#     wireLabel7='wire_label1_value',
#     otb7='otb1_value',
#     opoint7='opoint1_value',
#     dtb7='dtb1_value',
#     dpoint7='dpoint1_value',
#     # Repeat the same pattern for other parameters
# )
# print(update_result)
