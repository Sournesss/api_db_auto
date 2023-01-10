from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from myapi.filter_car.schemas import FilterCarSchema
from myapi.models import FilterCar
from myapi.extensions import db
from myapi.commons.pagination import paginate


class FilterCarResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - filter car
      summary: Get a filter car
      description: Get a single filter car by ID
      parameters:
        - in: path
          name: id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  filter_car: FilterCarSchema
        404:
          description: filter car does not exists
    put:
      tags:
        - filter car
      summary: Update a filter car
      description: Update a single filter car by ID
      parameters:
        - in: path
          name: id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              FilterCarSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: filter car updated
                  user: FilterCarSchema
        404:
          description: filter car does not exists
    delete:
      tags:
        - filter car
      summary: Delete a filter car
      description: Delete a single filter car by ID
      parameters:
        - in: path
          name: id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: filter car deleted
        404:
          description: filter car does not exists
    """

    # method_decorators = [jwt_required()]

    def get(self, user_id):
        schema = FilterCarSchema()
        user = FilterCar.query.get_or_404(user_id)
        return {"filter car": schema.dump(user)}

    def put(self, user_id):
        schema = FilterCarSchema(partial=True)
        user = FilterCar.query.get_or_404(user_id)
        user = schema.load(request.json, instance=user)

        db.session.commit()

        return {"msg": "filter car updated", "filter car": schema.dump(user)}

    def delete(self, id):
        user = FilterCar.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()

        return {"msg": "filter car deleted"}


class FilterCarList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - filter car
      summary: Get a list of filter cars
      description: Get a list of paginated filter cars
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/FilterCarSchema'
    post:
      tags:
        - filter car
      summary: Create a filter car
      description: Create a new filter car
      requestBody:
        content:
          application/json:
            schema:
              FilterCarSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: filter car created
                  user: FilterCarSchema
    """

    # method_decorators = [jwt_required()]

    def get(self):
        schema = FilterCarSchema(many=True)
        query = FilterCar.query
        return paginate(query, schema)

    def post(self):
        schema = FilterCarSchema()
        user = schema.load(request.json)

        db.session.add(user)
        db.session.commit()

        return {"msg": "filter car created", "filter car": schema.dump(user)}, 201
