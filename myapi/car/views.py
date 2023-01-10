from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from myapi.extensions import apispec
from myapi.car.resources import CarResource, CarList
from myapi.car.schemas import CarSchema


blueprint = Blueprint("car", __name__, url_prefix="/car")
api = Api(blueprint)


api.add_resource(CarResource, "/car/<int:car_id>", endpoint="car_by_id")
api.add_resource(CarList, "/cars", endpoint="cars")


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("CarSchema", schema=CarSchema)
    apispec.spec.path(view=CarResource, app=current_app)
    apispec.spec.path(view=CarList, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
