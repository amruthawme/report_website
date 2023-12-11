from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='/static',template_folder='templates')
# Set a secret key for session management
app.secret_key = 'wme2023'


# from flask import Flask
#
# # Create a placeholder for the app
# app = None
#
# def create_app():
#     global app
#     app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates')
#     app.secret_key = 'wme2023'
#
#     # No need to register blueprints for this example
#
#     return app



app.config['DEBUG'] = False
from app import views




