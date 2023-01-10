from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from myapi.car.schemas import CarSchema
from myapi.models import Car
from myapi.extensions import db
from myapi.commons.pagination import paginate


class CarResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - car
      summary: Get a car
      description: Get a single car by ID
      parameters:
        - in: path
          name: car_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  user: CarSchema
        404:
          description: car does not exists
    put:
      tags:
        - car
      summary: Update a car
      description: Update a single user by ID
      parameters:
        - in: path
          name: car_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              CarSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: car updated
                  user: CarSchema
        404:
          description: car does not exists
    delete:
      tags:
        - car
      summary: Delete a car
      description: Delete a single user by ID
      parameters:
        - in: path
          name: car_id
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
                    example: car deleted
        404:
          description: car does not exists
    """

    # method_decorators = [jwt_required()]

    def get(self, user_id):
        schema = CarSchema()
        car = Car.query.get_or_404(user_id)
        return {"car": schema.dump(car)}

    def put(self, user_id):
        schema = CarSchema(partial=True)
        car = Car.query.get_or_404(user_id)
        car = schema.load(request.json, instance=car)

        db.session.commit()

        return {"msg": "car updated", "car": schema.dump(car)}

    def delete(self, car_id):
        car = Car.query.get_or_404(car_id)
        db.session.delete(car)
        db.session.commit()

        return {"msg": "car deleted"}


class CarList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - car
      summary: Get a list of cars
      description: Get a list of paginated users
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
                          $ref: '#/components/schemas/CarSchema'
    post:
      tags:
        - car
      summary: Create a cars
      description: Create a new cars
      requestBody:
        content:
          application/json:
            schema:
              CarSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: car created
                  user: CarSchema
    """

    # method_decorators = [jwt_required()]

    def get(self):
        schema = CarSchema(many=True)
        query = Car.query
        return paginate(query, schema)

    def post(self):
        try:
            schema = CarSchema()
            # print(request.json)
            car = schema.load(request.json)
            db.session.add(car)
            db.session.commit()

            return {"msg": "car created", "car": schema.dump(car)}, 201
        except Exception as e:
            return {"msg":e,"car":""},500
