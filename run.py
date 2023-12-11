from flask import Flask, render_template, request, redirect, url_for, send_from_directory,flash
from flask import send_file
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import make_response
import ast
import json
import sys
import pandas as pd
import pyodbc
import script_upd
from app import app

from datetime import datetime
current_time = datetime.now()
#
#
#
# # print(f"Python Interpreter in Flask App: {sys.executable}")
# # print(f"pandas version in Flask App: {pd.__version__}")
# # print(f"pyodbc version in Flask App: {pyodbc.version}")
#
# # print(sys.executable)
#
if __name__ == '__main__':
    app.run(debug=True) # removed debug=True
#

# from app import create_app
#
# app = create_app()
#
# if __name__ == '__main__':
#     app.run(debug=True)
