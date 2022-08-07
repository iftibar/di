import os.path
import flask_bcrypt
from flask import flash, url_for, render_template, redirect, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, AddBusiness, UpdateCard
from app.models import User, Card
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def index():
    return redirect('/about')


@app.route('/mission')
def mission():
    return render_template('mission.html')


@app.route('/about')
def about():
    cards = Card.query.all()
    images = {}
    likes = {}
    for card in cards:
        images[card.email] = url_for('static', filename='uploads/' + card.email + '.jpg')
        card.liked = current_user in card.liked_by
        likes[card.email] = len(card.liked_by)

    return render_template('about.html', cards=cards, images=images,  likes=likes)


@app.route('/<card_id>/like', methods=['GET', 'POST'])
def like(card_id):
        card = Card.query.filter_by(id=card_id).first_or_404()
        if current_user not in card.liked_by:
            card.liked_by.append(current_user)
            db.session.commit()
        return redirect(request.referrer)


@app.route('/<card_id>/unlike', methods=['GET', 'POST'])
def unlike(card_id):
    card = Card.query.filter_by(id=card_id).first_or_404()
    if current_user in card.liked_by:
        card.liked_by.remove(current_user)
        db.session.commit()
    return redirect(request.referrer)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = flask_bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash(f'Account was created for {form.name.data} you can log in now', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and flask_bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            elif current_user.card:
                return redirect(url_for('account', user=user))
            else:
                return redirect(url_for('create_card', user=user))
        else:
            flash('login was unsuccessful, check email and password', 'danger')
    return render_template('login.html', title='login', form=form)


@app.route('/create', methods=['GET', 'POST'])
def create_card():
    form = AddBusiness()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        phone = form.phone.data
        email = form.email.data
        website = form.website.data
        facebook = form.facebook.data
        address = form.address.data
        sentence = form.sentence.data
        file = request.files['file']
        if file:
            filename = current_user.email + '.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user = User.query.filter_by(email=current_user.email).first()
        new_card = Card(name=name, category=category, phone=phone, email=email,
                        website=website, facebook=facebook, address=address, sentence=sentence, user=[user])
        db.session.add(new_card)
        db.session.commit()
        return redirect('/account')
    return render_template('create_card.html', form=form, user=current_user)



@app.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateCard()
    card = Card.query.filter_by(email=current_user.email).first()
    if form.validate_on_submit():
        card.name = form.name.data
        card.category = form.category.data
        card.phone = form.phone.data
        card.email = form.email.data
        card.website = form.website.data
        card.facebook = form.facebook.data
        card.address = form.address.data
        card.sentence = form.sentence.data
        file = request.files['file']
        if file:
            filename = current_user.email + '.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        db.session.add(card)
        db.session.commit()
        return redirect('/account')
    return render_template('update.html', form=form, user=current_user, card=card)


@app.route("/account")
@login_required
def account():
    card = Card.query.filter_by(email=current_user.email).first()
    if not card:
        return redirect("/create")
    img = url_for('static', filename='uploads/' + current_user.email + '.jpg')
    return render_template('account.html', title='account', card=card, user=current_user, img=img)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('about'))
