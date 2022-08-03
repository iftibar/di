from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"
app.config['UPLOAD_FOLDER'] = r'C:\Users\user\Desktop\DI\final project\app\static\uploads'


bcrypt = Bcrypt(app)
login_mngr = LoginManager(app)
login_mngr.login_view = 'login'


# Database Connection
db_info = {'host': 'localhost',
		   'database': 'prolo_final',
		   'psw': 'krembo58',
		   'user': 'postgres',
		   'port': ''}

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes
