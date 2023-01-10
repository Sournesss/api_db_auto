from myapi.models import Car
from myapi.extensions import ma, db
import datetime


class CarSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int()
    color = ma.String()
    age = ma.Int()
    price = ma.Int()
    brand = ma.String()
    model = ma.String()
    geo = ma.String()
    description = ma.String()
    mileage = ma.Int()
    time_publication = ma.DateTime(format='%Y-%m-%d %H:%M:%S')
    time_parser = ma.DateTime(format='%Y-%m-%d %H:%M:%S')
    url = ma.String()

    class Meta:
        model = Car
        sqla_session = db.session
        load_instance = True
        # datetimeformat = '%Y-%m-%d'
