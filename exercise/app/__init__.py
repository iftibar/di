import flask

app_flask = flask.Flask(__name__)
app_flask.config['SECRET_KEY'] = 'the random string'

from exercise.app import routes
