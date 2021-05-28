from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) #index is used when you want to be able to search the db for item
    email = db.Column(db.String(120), index=True, unique=True) #unique stops it from accepting duplicates
    password_hash = db.Column(db.String(128))
    subscriptions = db.relationship('Subscriptions', backref='subscriptions', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    company = db.Column(db.String(20))
    description = db.Column(db.String(120))
    # price = db.Column(db.Integer())
    # next_payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    # payment_frequency = db.Column(db.Integer())
    # category = db.Column(db.String(50))

    def __repr__(self):
        return f'<Subscription {self.company}>'
