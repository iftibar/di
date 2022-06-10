import flask
import database_manager  # this is our module

app = flask.Flask(__name__)
database_manager.create_database()


@app.route("/")
@app.route("/products")
def products_page():
	data = database_manager.load_database()
	# css = open('static/style.css', 'r').read()
	# return flask.render_template("my_template.html", products=data, additional_css=css)

	return flask.render_template("my_template.html", products=data)


app.run(debug=True)
