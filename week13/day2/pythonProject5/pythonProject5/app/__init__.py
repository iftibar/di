import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flask_app = flask.Flask(__name__)  # Remember: __name__ is the name of the file where the code is written

# Database Connection
db_info = {
	'host': 'localhost',
	'database': 'bookstore',
	'psw': '1234',
	'user': 'postgres',
	'port': ''
}

flask_app.config[
	'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from app import routes, models
