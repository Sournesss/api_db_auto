from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from myapi.extensions import apispec
from myapi.filter_car.resources import FilterCarResource, FilterCarList
from myapi.filter_car.schemas import FilterCarSchema


blueprint = Blueprint("filter", __name__, url_prefix="/filter")
api = Api(blueprint)


api.add_resource(FilterCarResource, "/filter/<int:filter_car_id>", endpoint="filter_car_by_id")
api.add_resource(FilterCarList, "/filters", endpoint="filters")


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("FilterCarSchema", schema=FilterCarSchema)
    apispec.spec.path(view=FilterCarResource, app=current_app)
    apispec.spec.path(view=FilterCarList, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
