from sqlalchemy.ext.hybrid import hybrid_property

from myapi.extensions import db
from datetime import datetime
from myapi.models import User
from sqlalchemy.orm import backref


class FilterCar(db.Model):
    """Basic filter car model"""

    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User, backref=backref('filtercar', uselist=False))
    color = db.Column(db.String(80))
    age = db.Column(db.Integer)
    min_price = db.Column(db.Integer)
    max_price = db.Column(db.Integer)
    brand = db.Column(db.String(80))
    model = db.Column(db.String(80))
    geo = db.Column(db.String(80))
    description = db.Column(db.String())
    mileage = db.Column(db.Integer)
    time_create = db.Column(db.DateTime)
    url = db.Column(db.String(80))





    def __repr__(self):
        return f'id filter car -> {self.id} {self.color} {self.user.id}'
