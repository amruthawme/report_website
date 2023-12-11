# from app import app
# from app import create_app

from run import app
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,flash
from flask import send_file
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import make_response
import ast
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)
import config
import json
import sys
import pandas as pd
import pyodbc
from flask import jsonify
import script_upd
from datetime import datetime
current_time = datetime.now()

# app = create_app()

login_manager = LoginManager()
login_manager.login_view = "login"  # The login view
login_manager.init_app(app)
user_credentials = {
    'username1': 'password1',
    'username2': 'password2',
    # Add more username-password pairs as needed
}

ALLOWED_EXTENSIONS = {'csv', 'txt', 'xlsx'}  # Add allowed extensions here

# Define the upload folder and allowed file extensions
UPLOAD_FOLDER = 'uploads'
GENERATED_REPORTS = []  # New list to track generated reports


print(os.path)
# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class User(UserMixin):
    def __init__(self, id):
        self.id = id


# Set cache control headers for static assets
@app.after_request
def add_cache_control(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return response

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# The /login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the provided username and password are valid
        if username in user_credentials and user_credentials[username] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('upload_form'))  # Redirect to your main page
        else:
            #return 'Invalid username or password'  # Display an error message
            return redirect(url_for('login', error='true'))

    return render_template('login.html')
    # response = make_response(render_template('login.html'))
    # return no_cache_response(response)


# Custom middleware to check if the user is logged in
@app.before_request
def check_user_login():
    if request.endpoint != 'login' and not current_user.is_authenticated:
        #flash('Please log in first', 'error')  # Unauthorized access message
        return redirect(url_for('login'))

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Custom response to prevent caching
def no_cache_response(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response



# Route to display the main page
@app.route('/')
@login_required
def upload_form():
    #return render_template('upload.html')
    response = make_response(render_template('upload.html'))
    return no_cache_response(response)

@app.route('/get_databases', methods=['GET'])
def get_dblist():
    # Put the code here to run your other Python program
    # For example, you can use the subprocess module to run it
    import subprocess
    import sys

    try:
        # Use sys.executable to specify the Python interpreter
        result = subprocess.run(
            [sys.executable, 'scripts/script_db.py'],
            capture_output=True,
            text=True,
            check=True
        )

        output = result.stdout
        error_output = result.stderr

        output = result.stdout

        # Split the output by newlines
        lines = output.split('\n')
        #
        # # Assuming the list is on the second line (index 1), you can safely evaluate it
        # try:
        #     result_list = ast.literal_eval(lines[1])
        #     print(result_list)
        #     return result_list
        #
        # except (SyntaxError, ValueError) as e:
        #     print("Error parsing the list:", e)
    #     #return 'Other program executed successfully. Output:\n' + output
    #     return output
        try:
            result_list = ast.literal_eval(lines[1])
            print(result_list)
            # return result_list
            return jsonify(result_list)
        except (SyntaxError, ValueError) as e:
            print("Error parsing the list:", e)
            # Return an appropriate response, e.g., an error message
            return jsonify({'error': 'Invalid JSON format'}), 500
    except subprocess.CalledProcessError as e:
        return 'Error executing the other program. Error:\n' + e.stderr

# @app.route('/get_databases', methods=['GET'])
# def get_dblist():
#     import subprocess
#     try:
#         # Use sys.executable to specify the Python interpreter
#         result = subprocess.run(
#             [sys.executable, 'scripts/script_db.py'],
#             capture_output=True,
#             text=True,
#             check=True
#         )
#
#         output = result.stdout
#         error_output = result.stderr
#
#         output = result.stdout
#
#         # Split the output by newlines
#         lines = output.split('\n')
#
#         # Assuming the list is on the second line (index 1), you can safely evaluate it
#         try:
#             result_list = ast.literal_eval(lines[1])
#             print(result_list)
#             # Convert the Python list to a JSON-formatted string using jsonify
#             return jsonify(result_list)
#
#         except (SyntaxError, ValueError) as e:
#             print("Error parsing the list:", e)
#             # Return a JSON response with an error message
#             return jsonify({'error': 'Error parsing the list'}), 500
#
#     except subprocess.CalledProcessError as e:
#         # Return a JSON response with an error message
#         return jsonify({'error': 'Error executing the other program'}), 500

@app.route('/update_config', methods=['POST'])
def upd_config():
    # Get the values submitted from the form
    server = request.form.get('server')
    table_name = request.form.get('table_name')
    database = request.form.get('database_select') or request.form.get('manual_database')

    # Update the config file with the new values
    config_path = 'config.py'
    with open(config_path, 'w') as config_file:
        config_file.write(f"server = '{server}'\n")
        config_file.write(f"database = '{database}'\n")
        config_file.write(f"table_name = '{table_name}'\n")
        config_file.write(f"driver = '{{SQL Server}}'\n")
        config_file.write(f"report1_name = 'wire_label.xlsx'\n")
        config_file.write(f"report2_name = 'cabel_label.xlsx'\n")
        config_file.write(f"report3_name = 'status_report.xlsx'\n")
        config_file.write(f"report4_name = 'modified_status_report.xlsx'\n")
    return "Config updated successfully"


# Route to handle file upload

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        # Save the uploaded file to the UPLOAD_FOLDER
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        # Optionally, you can redirect to a success page or perform other actions here
        return 'File successfully uploaded!'
    else:
        return 'Invalid file format or no file selected.'


# # Route to handle running the other program
# @app.route('/run_other_program', methods=['POST'])
# def run_other_program():
#     # Put the code here to run your other Python program
#     # For example, you can use the subprocess module to run it
#     import subprocess
#     try:
#         # Replace 'python_script.py' with the actual filename of your other program
#         result = subprocess.run(
#             ['python', 'C:/Users/amrutha.shetty/PycharmProjects/setup_prog/script.py'],
#             capture_output=True,
#             text=True,
#             check=True
#         )
#
#         output = result.stdout
#         error_output = result.stderr
#         #return 'Other program executed successfully. Output:\n' + output
#         return output
#     except subprocess.CalledProcessError as e:
#         return 'Error executing the other program. Error:\n' + e.stderr

# Route to handle running the other program
@app.route('/run_other_program', methods=['POST'])
def run_other_program():
    # Put the code here to run your other Python program
    # For example, you can use the subprocess module to run it
    import subprocess
    import sys

    try:
        # Use sys.executable to specify the Python interpreter
        result = subprocess.run(
            [sys.executable, 'scripts/script.py'],
            capture_output=True,
            text=True,
            check=True
        )

        output = result.stdout
        error_output = result.stderr
        #return 'Other program executed successfully. Output:\n' + output
        return output
    except subprocess.CalledProcessError as e:
        return 'Error executing the other program. Error:\n' + e.stderr

#@app.route('/generate_report', methods=['POST'])
# def generate_report():
#     # Put the code here to run your other Python program
#     # For example, you can use the subprocess module to run it
#     import subprocess
#     import sys
#
#     try:
#         # Use sys.executable to specify the Python interpreter
#         result = subprocess.run(
#             [sys.executable, 'C:/Users/amrutha.shetty/PycharmProjects/setup_prog/script_report_1.py'],
#             capture_output=True,
#             text=True,
#             check=True
#         )
#
#         output = result.stdout
#         error_output = result.stderr
#         #return 'Other program executed successfully. Output:\n' + output
#         return output
#     except subprocess.CalledProcessError as e:
#         return 'Error executing the other program. Error:\n' + e.stderr

@app.route('/generate_report', methods=['POST'])
def generate_report():
    import subprocess
    import sys
    # List of script paths to execute
    script_paths = [
        'scripts/script_report_1.py',
        'scripts/script_report_2.py',
        #'C:/Users/amrutha.shetty/PycharmProjects/setup_prog/script_report_3.py',
        # Add more script paths as needed
    ]

    # Initialize an empty result list to store outputs
    results = []

    # Iterate through the list of script paths and run each script
    for script_path in script_paths:
        try:
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                check=True
            )
            output = result.stdout
            results.append(f'Success: {script_path}\n{output}')
        except subprocess.CalledProcessError as e:
            error_output = e.stderr
            results.append(f'Error: {script_path}\n{error_output}')

    # Return the results as a newline-separated string
    return '\n'.join(results)

@app.route('/generated_reports')
def list_generated_reports():
    # Get a list of all files in the directory where reports are stored
    reports_dir = 'reports'  # Replace with the actual path
    reports_list = os.listdir(reports_dir)
    return render_template('generated_reports.html', reports=reports_list)

@app.route('/download_report/<filename>')
def download_report(filename):
    # Set the path to the reports directory
    reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')

    # Return the file as an attachment for download
    return send_from_directory(reports_dir, filename, as_attachment=True)

# Define the route for the status report page
@app.route('/generate_status_report', methods=['GET', 'POST'])
def status_report_steps():
    if request.method == 'POST':
        # Handle the form submission here (database and dataset name)
        database_name = request.form['database_name']
        dataset_name = request.form['dataset_name']

        # Generate the .rdl file based on the database and dataset
        rdl_file_path = generate_rdl(database_name, dataset_name,"status_reports/status_report_mod.rdl")

        # Return the .rdl file to the user
        return send_file(rdl_file_path, as_attachment=True)

    # Render the status report page with instructions
    title = "Status Report"
    description = "Please follow the below steps to generate the status report:<br>" \
                  "<br>"\
                  "1. Enter the name of the database and dataset (table) you want to generate a report for. <br>" \
                  "2. Click the 'Generate .rdl file' button on the right to download the .rdl file.<br>" \
                  "3. Open SQL Server Management Studio (SSMS) on your system.<br>" \
                  "<img src='static/ssms_logo.jpg' width='60' height='60'><br>" \
                  "4. In SSMS, right-click on the database name.<br>" \
                  "5. Select 'Reports' from the context menu.<br>" \
                  "6. Choose 'Custom Reports' from the options.<br>" \
                  "7. Upload the .rdl file you downloaded earlier.<br>" \
                  "8. Click 'RUN' on the 'Run Custom Report' notification.<br>" \
                  "9. Once the report is displayed, simply right-click on it and export the file in your preferred format.<br>"

    return render_template('generate_status_report.html', title="Status Report", description=description)


# @app.route('/change')
# def change():
#     # Your code to render the change.html template
#     with open('temp.txt', 'r') as file:
#         column_values = json.load(file)
#     return render_template('change.html', unique_values=column_values)
#
session = {}
@app.route('/change', methods=['GET', 'POST'])
def change():
    if request.method == 'POST':
        # Handle form submission (update values based on Cable_Tag)
        cable_tag = request.form.get('cableTag')
        session['cable_tag'] = cable_tag  # Store cable_tag in session
        cable_values = get_cable_values_for_tag(cable_tag)
        return render_template('change.html', cableTag=cable_tag, cable_values=cable_values)


    # Render the change.html template without form submission
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('change.html', cableTag=None, cable_values=None, formatted_time=formatted_time)

# @app.route('/change', methods=['GET', 'POST'])
# def change():
#     if request.method == 'POST':
#         cable_tag = request.form.get('cableTag')
#         # Fetch cable values based on cable_tag (you need to implement this logic)
#         cable_values = get_cable_values_for_tag(cable_tag)
#         return render_template('change.html', cable_values=cable_values, cableTag=cable_tag)
#     return render_template('change.html', cableTag=None, cable_values=None)


# Function to get cable values based on Cable_Tag
def get_cable_values_for_tag(cable_tag):
    # Your logic to fetch cable values from temp.txt based on the cable_tag
    # Load the temp.txt file and extract values for the specified cable_tag
    with open('temp.txt', 'r') as file:
        all_cable_values = json.load(file)

    # Check if the cable_tag exists in the dictionary
    if cable_tag in all_cable_values:
        return all_cable_values[cable_tag]

    # Return an empty dictionary or handle the case when cable_tag is not found
    return {}

@app.route('/update_database', methods=['POST'])
def update_database():
    data = request.get_json()
    cableTag = session.get('cable_tag')  # Retrieve cable_tag from session
    if cableTag is None:
        return "Error: Cable tag not found in session."
    change = data.get('change')
    notes = data.get('notes')
    dynamic_fields = {}
    for i in range(1, 8):
        dynamic_fields[f'color{i}'] = data.get(f'Color{i}')
        dynamic_fields[f'wireLabel{i}'] = data.get(f'Wire_Label{i}')
        dynamic_fields[f'otb{i}'] = data.get(f'OTB{i}')
        dynamic_fields[f'opoint{i}'] = data.get(f'OPoint{i}')
        dynamic_fields[f'dtb{i}'] = data.get(f'DTB{i}')
        dynamic_fields[f'dpoint{i}'] = data.get(f'DPoint{i}')



    # Call the script_upd.py with the data to update the database
    # You may need to adjust this based on the structure of your script_upd.py
    result = script_upd.update_database(cableTag, change,notes, **dynamic_fields)
    return result

@app.route('/generate_modified_report', methods=['GET', 'POST'])
def generate_modified_report():
    if request.method == 'POST':
        import subprocess
        import sys
        try:
            # Use sys.executable to specify the Python interpreter
            result = subprocess.run(
                [sys.executable, 'scripts/script_report_4.py'],
                capture_output=True,
                text=True,
                check=True
            )

            output = result.stdout
            error_output = result.stderr
            # return 'Other program executed successfully. Output:\n' + output
            #return output
            # Generate the .rdl file based on the database and dataset

        except subprocess.CalledProcessError as e:
            #return 'Error executing the other program. Error:\n' + e.stderr
            print('Error executing the other program. Error:\n' + e.stderr)

        #updated table name

        rdl_file_path = generate_rdl(config.database, 'newtable', 'status_reports/upd_status_report_mod.rdl')

        # Return the .rdl file to the user
        return send_file(rdl_file_path, as_attachment=True)




    # Return the results as a newline-separated string
    # return '\n'.join(results)

def generate_rdl(database_name, dataset_name,rdl_file_path):
    # Include the code to generate the .rdl file based on the provided database_name and dataset_name

    # Define the path to the .rdl file
    rdl_file_path = rdl_file_path

    # Read the .rdl file
    with open(rdl_file_path, 'r', encoding='utf-8') as rdl_file:
        rdl_content = rdl_file.read()

    # Replace placeholders with user input
    rdl_content = rdl_content.replace('DataSource2', dataset_name)
    rdl_content = rdl_content.replace('DataSet1', database_name)

    # Save the modified .rdl file
    modified_rdl_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'status_report.rdl')
    with open(modified_rdl_file_path, 'w', encoding='utf-8') as modified_rdl_file:
        modified_rdl_file.write(rdl_content)

    return modified_rdl_file_path


# Route to handle logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    #return redirect(url_for('login'))
    response = make_response(redirect(url_for('login')))
    return no_cache_response(response)
