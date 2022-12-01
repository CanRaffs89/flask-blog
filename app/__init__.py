import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

ENV = 'prod'

if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DEV_DB_URI")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("PROD_DB_URI")

app.config['SECRET_KEY'] = os.getenv("KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
ckeditor = CKEditor(app)

from app import routes