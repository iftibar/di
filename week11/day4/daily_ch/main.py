import flask

app = flask.Flask(__name__)

@app.route("/")
def homepage():

	return flask.render_template("homepage.html")


app.run(debug=True)
