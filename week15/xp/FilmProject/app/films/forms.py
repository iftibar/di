from datetime import datetime as dt
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField


class AddFilmForm (FlaskForm):
    title = StringField('title')
    release_date = DateTimeField('release_date', default=dt.now().date())
    created_in_country = SelectField('created_in_country', choices=["usa", "israel", "nowhere", "china"])
    # available_in_countries = StringField('available_in_countries')
    category = SelectField('category',  choices=["comedy", "drama", "thriller"])
    submit = SubmitField('submit')


class AddDirectorForm(FlaskForm):
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    film = SelectField('film',  choices=["hustle", "batman", "avatar"])
    submit = SubmitField('submit')
