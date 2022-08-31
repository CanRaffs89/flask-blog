from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgrespass@localhost/blog'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cipefqatmcxywj:081a7fdfa6fdebff523a8570d788afb0f2f31b4438cd1b077f655a42cf3169f2@ec2-54-205-61-191.compute-1.amazonaws.com:5432/ddedfg2rqcr5pu'

app.config['SECRET_KEY'] = '40014fa522110b5a21b52cca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
ckeditor = CKEditor(app)

from app import routes