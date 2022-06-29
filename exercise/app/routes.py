import flask
from exercise.app import app_flask
from flask import flash, render_template

@app_flask.route("/")
def index():
    flash("this is not working", "error")
    flash("Logged in successfully", "success")
    flash("this is one flashed message!")
    return flask.render_template('index.html')