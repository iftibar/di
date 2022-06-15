import flask
from xp import app

@app.route("/")
def index():
    posts = [
        {"author":"John", "body":"I love python"},
        {"author":"Fish", "body":"I love water"},
        {"author":"Herpetolog", "body":"I love pythons"},
    ]
    return flask.render_template('index.html',posts=posts)