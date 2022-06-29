from week13.day2.xp.app import flask_app, db
from week13.day2.xp.app.models import User
from flask import redirect, render_template


@flask_app.route('/')
def index():
   print("Hello")
   return "h"