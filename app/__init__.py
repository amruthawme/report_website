from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='/static',template_folder='templates')
# Set a secret key for session management
app.secret_key = 'wme2023'

from app import views
