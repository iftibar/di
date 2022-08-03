from app.films import flask_app, db
from flask import redirect, render_template, session
from app.films.forms import AddFilmForm, AddDirectorForm
from app.films.models import Film, Director, Country, Category


@flask_app.route('/')
@flask_app.route('/homepage')
def home():
    films = Film.query.all()
    return render_template('homepage.html', films=films)


@flask_app.route('/film/addFilm', methods=['GET', 'POST'])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        title = form.title.data
        release_date = form.release_date.data
        created_in_country = Country.query.filter_by(name=form.created_in_country.data).first()
        # available_in_countries = form.available_in_countries.data
        # category = form.category.data
        available_countries = [Country.query.filter_by(name=form.created_in_country.data).first()]
        # directors = [Director.query.get(name=form.director.data)]
        category = [Category.query.filter_by(name=form.category.data).first()]
        new_film = Film(title=title, release_date=release_date, created_in_country=created_in_country.id,
                        categories=category, available_in_countries=available_countries)
        db.session.add(new_film)
        db.session.commit()
        films = Film.query.all()
        return render_template('homepage.html', films=films)
    return render_template('film/addFilm.html', form=form)



@flask_app.route('/film/addDirector', methods=['GET', 'POST'])
def add_director():
    form = AddDirectorForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        film = form.film.data
        director = Director(first_name=first_name, last_name=last_name, film=film)
        db.session.add(director)
        db.session.commit()
        return render_template('homepage.html', director=director)
    return render_template('director/addDirector.html', form=form)

