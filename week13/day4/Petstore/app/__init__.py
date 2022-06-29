from flask import Flask


from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = "123"

# Database Connection
db_info = {'host': 'localhost',
           'database': 'petstore',
           'psw': 'krembo58',
           'user': 'postgres',
           'port': ''}
flask_app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

