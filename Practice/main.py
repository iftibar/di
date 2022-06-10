
import flask
app = flask.Flask(__name__)

art_list = [{
    "title": "article1",
    "content": "article1 content",
    "author": "article1 author"
},
{
    "title": "article2",
    "content": "article2 content",
    "author": "article2 author"
}]


@app.route('/')
def index():
    my_template = '''
          <html>
              <head>
                  <title>Home Page - Microblog</title>
              </head>
              <body>
                   <h1>{{ firstname }} {{ lastname }} says: Wubbalubbadubdub!</h1>
              </body>
          </html>
      '''

    html = flask.render_template_string(my_template, firstname="Rick", lastname="Sanchez")
    return html

@app.route('/blog')
def blog():
    with open('homepage.html') as f:
        return f.read()


@app.route('/blog/articles')
def articles():
    with open("articles.html") as f:
        return flask.render_template_string(f.read(), articles=art_list)


@app.route('/some')
def move():
    return flask.redirect(flask.url_for('articles'))

@app.route('/profile')
def profile():
    return flask.redirect(flask.url_for('blog'))


app.run(debug=True)