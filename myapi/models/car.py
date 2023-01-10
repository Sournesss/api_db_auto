from myapi.extensions import db
from datetime import datetime


class Car(db.Model):
    """Basic filter car model"""

    id = db.Column(db.Integer, unique=True, primary_key=True)
    color = db.Column(db.String(80))
    age = db.Column(db.Integer)
    price = db.Column(db.Integer)
    brand = db.Column(db.String(80))
    model = db.Column(db.String(80))
    geo = db.Column(db.String(80))
    description = db.Column(db.String())
    mileage = db.Column(db.Integer)
    time_publication = db.Column(db.DateTime)
    time_parser = db.Column(db.DateTime)
    url = db.Column(db.String(80))





    def __repr__(self):
        return f'id car -> {self.id}'
