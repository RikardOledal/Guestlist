from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

application_name = "The Guestlist"
version = "1.0"

welcome_message = "Welcome to the {0}. Version v{1}!".format(application_name, version)

app = Flask(__name__)