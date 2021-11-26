import uuid
from flasgger import Swagger
from flasgger import swag_from
from flask import Flask, jsonify, request
from marshmallow.exceptions import ValidationError
from schemas import ProductSchema, ProductEditSchema

app = Flask(__name__)
swagger = Swagger(app)
app.config['JSON_SORT_KEYS'] = False

products = [{'id': uuid.uuid4().hex, 'name': 'First Product', 'price': 81.54, 'description': 'XXXXXX', 'inventory': 15}]


@app.route('/products', methods=['GET'])
@swag_from({
    'tags': ['Products'],
    'responses': {
        200: {
            'schema': ProductSchema
        }
    }
})
def listing():
    """
    List
    """
    return jsonify({'data': products}), 200


@app.route('/products', methods=['POST'])
@swag_from({
    'tags': ['Products'],
    'parameters': [{
        'in': 'body',
        'name': 'body',
        'required': True,
        'schema': ProductSchema
    }],
    'responses': {
        201: {
            'schema': ProductSchema
        },
        422: {
            'schema': ProductSchema
        }

    }
})
def create():
    try:
        data = ProductSchema().load(request.json)
        product = dict(ProductSchema().dump(data))
        products.append(product)

        return jsonify({'data': product}), 201
    except ValidationError as e:
        print(e)
        errors = {'message': 'Unprocessable Entity', 'errors': e.messages}
        return jsonify(errors), 422


@app.route('/products/<string:prod_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Products'],
    'parameters': [{
        'in': 'body',
        'name': 'body',
        'required': True,
        'schema': ProductEditSchema
    }],
    'responses': {
        200: {
            'schema': ProductEditSchema
        },
        404: {
            'schema': ProductEditSchema
        },
        422: {
            'schema': ProductEditSchema
        }
    }
})
def edit(prod_id):
    try:
        for product in products:
            if product['id'] == prod_id:
                data = ProductEditSchema().load(request.json)
                data = dict(ProductEditSchema().dump(data))
                product.update(**data)

                return jsonify({'data': product}), 200

        return jsonify({'message': 'Register Not Found.'}), 404
    except ValidationError as e:
        print(e)
        errors = {'message': 'Unprocessable Entity', 'errors': e.messages}
        return jsonify(errors), 422


@app.route('/products/<string:prod_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Products'],
    'parameters': [{
        'in': 'body',
        'name': 'body',
        'required': True,
        'schema': ProductSchema
    }],
    'responses': {
        204: {
            'schema': ProductSchema
        },
        404: {
            'schema': ProductSchema
        }
    }
})
def delete(prod_id):
    x = 0
    for product in products:
        if product['id'] == prod_id:
            del products[x]

            return '', 204

        x += 1

    return jsonify({'message': 'Register Not Found.'}), 404
