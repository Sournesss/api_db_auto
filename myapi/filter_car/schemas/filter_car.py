from myapi.models import FilterCar
from myapi.extensions import ma, db


class FilterCarSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    color = ma.String()
    age = ma.Int()
    min_price = ma.Int()
    max_price = ma.Int()
    brand = ma.String()
    model = ma.String()
    geo = ma.String()
    description = ma.String()
    mileage = ma.Int()
    time_create = ma.DateTime(format='%Y-%m-%d %H:%M:%S')
    url = ma.String()

    class Meta:
        model = FilterCar
        sqla_session = db.session
        load_instance = True
        # exclude = ("_password",)
