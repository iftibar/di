from week13.day2.xp.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    street = db.Column(db.String(64))
    city = db.Column(db.String(64))
    zipcode = db.Column(db.String(64))



