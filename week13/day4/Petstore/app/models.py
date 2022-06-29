from datetime import time

from app import db


class Pet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	gender = db.Column(db.string(1))
	breed = db.Column(db.string(64))
	date_of_birth = db.Column(db.date, default=time.today)
	details = db.Column(db.string(64))
	price = db.Column(db.Integer)
	image = db.Column(db.string(64))


