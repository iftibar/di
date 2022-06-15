import flask

app = flask.Flask(__name__)

@app.route("/")
def homepage():
	html = flask.render_template("homepage.html")
	return html


app.run(debug=True)
