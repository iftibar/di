from app import db, login_mngr
from flask_login import UserMixin

@login_mngr.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


user_like_card = db.Table('user_like_card',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('card_id', db.Integer, db.ForeignKey('card.id')))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    card = db.Column(db.Integer, db.ForeignKey('card.id'))
    likes = db.relationship("Card", secondary=user_like_card, back_populates='liked_by')


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    category = db.Column(db.String(64))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(64))
    website = db.Column(db.String(64))
    facebook = db.Column(db.String(64))
    address = db.Column(db.String(64))
    sentence = db.Column(db.String(64))
    user = db.relationship("User", backref='card_user', lazy=True)
    liked_by = db.relationship("User", secondary=user_like_card, back_populates='likes')

