
import flask
import flask_wtf
import wtforms

app = flask.Flask(__name__)


app.config['SECRET_KEY'] = 'you-will-never-guess'


class Form(flask_wtf.FlaskForm):
    first_name = wtforms.StringField("first_Name")
    last_name = wtforms.StringField("last_name")
    age = wtforms.TelField("age")
    submit = wtforms.SubmitField("Submit")


@app.route('/form')
def form():
    form = Form()
    return flask.render_template_string("homepage.html", form=form)

app.run()