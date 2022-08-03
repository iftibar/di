from datetime import datetime as dt
from app.films import db


films_table_country = db.Table('films_country',
                      db.Column('country_id', db.Integer, db.ForeignKey('country.id')),
                      db.Column('film_id', db.Integer, db.ForeignKey('film.id')))

films_table_category = db.Table('films_category',
                       db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
                       db.Column('film_id', db.Integer, db.ForeignKey('film.id')))

films_table_director = db.Table('films_director',
                       db.Column('director_id', db.Integer, db.ForeignKey('director.id')),
                       db.Column('film_id', db.Integer, db.ForeignKey('film.id')))


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    films = db.relationship('Film', backref='country', lazy='dynamic')


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    films = db.relationship('Film', secondary=films_table_category, back_populates="categories")


class Film(db.Model):
    # date = db.Column(db.DateTime, default=dt.now().strftime("%d %m %Y"))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    release_date = db.Column(db.DateTime, default=dt.now().strftime("%d %m %Y"))
    created_in_country = db.Column(db.Integer, db.ForeignKey('country.id'))
    available_in_countries = db.relationship("Country", secondary=films_table_country)
    categories = db.relationship("Category", secondary=films_table_category, back_populates='films')
    # director = db.relationship("Director", secondary=films_table_director)


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    film = db.Column(db.String(64))

