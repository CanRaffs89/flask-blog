from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password123@localhost/flask_blog'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://flask_blog_database_v8lr_user:D2p8Q7IooHrdT8gRISX0IliTnsZuq9Ws@dpg-ce3sanha6gdqkro3ckbg-a.frankfurt-postgres.render.com/flask_blog_database_v8lr'

app.config['SECRET_KEY'] = '40014fa522110b5a21b52cca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
ckeditor = CKEditor(app)

from app import routes