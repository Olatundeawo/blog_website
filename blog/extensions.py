from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_mail import Mail, Message
# from flask_oauthlib.client import OAuth

db = SQLAlchemy()
ckeditor = CKEditor()
login_manager = LoginManager()
mail = Mail()
# oauth = OAuth()