from random import random

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = '1234'
flask_app.config['DEBUG'] = True
os.system('export FLASK_APP=run.py')

db_info = {'host': 'localhost',
           'database': 'robots',
           'psw': '1234',
           'user': 'postgres',
           'port': ''}
flask_app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from week13.day2.xp.app import routes, models
