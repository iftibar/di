from flask import Flask
# Flask Object
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"

# Database Connection
db_info = {'host': 'localhost',
		   'database': 'bookstore',
		   'psw': 'krembo58',
		   'user': 'postgres',
		   'port': ''}

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes
