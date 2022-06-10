import flask

app = flask.Flask(__name__)

articles_lst = [
	{
		"title": "article1 title",
		"content": "article1 content",
		"author": "article1 author",
	},
	{
		"title": "article2 title",
		"content": "article2 content",
		"author": "article2 author",
	},
	{
		"title": "article3 title",
		"content": "article3 content",
		"author": "article3 author",
	},
	{
		"title": "article4 title",
		"content": "article4 content",
		"author": "article4 author",
	}
]


@app.route('/blog/articles')
def articles():
	return flask.render_template("articles.html", articles=articles_lst)


@app.route('/blog/<username>')
def blog(username):
	return flask.render_template("homepage.html", name=username)


@app.route('/profile')
def profile():
	return flask.redirect(flask.url_for('blog'))


if __name__ == "__main__":
	app.run()
