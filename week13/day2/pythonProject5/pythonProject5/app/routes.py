from app import flask_app
from app.models import Book


@flask_app.route('/')
def index():
	books = ', '.join([book.title for book in Book.query.all()])
	return books
