from flask import Blueprint, request, jsonify
from src.application.repositories.product_repository import ProductRepository

product_blueprint = Blueprint('product_bp', __name__)

# Create a new product
@product_blueprint.route('/api/product/', methods=['POST'])
def create_product():
    """
    Create a new product
    ---
    tags:
      - Product
    parameters:
      - name: body
        in: body
        required: True
        schema:
          type: object
          properties:
            name:
              type: string
            price:
              type: number
            amount:
              type: integer
    responses:
      201:
        description: Product created successfully
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        amount = data.get('amount')
        new_product = ProductRepository.create_product(name, price, amount)
        return jsonify(new_product.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a specific product by ID
@product_blueprint.route('/api/product/<int:product_id>/', methods=['GET'])
def get_product(product_id):
    """
    Get a specific product by ID
    ---
    tags:
      - Product
    parameters:
      - name: product_id
        in: path
        type: integer
        required: True
    responses:
      200:
        description: Product retrieved successfully
      404:
        description: Product not found
      500:
        description: Internal server error
    """
    try:
        product = ProductRepository.get_product(product_id)
        if product:
            return jsonify(product.to_dict()), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a list of products with pagination
@product_blueprint.route('/api/product/', methods=['GET'])
def get_products():
    """
    Get a list of products with pagination
    ---
    tags:
      - Product
    parameters:
      - name: skip
        in: query
        type: integer
        required: False
      - name: limit
        in: query
        type: integer
        required: False
    responses:
      200:
        description: Products retrieved successfully
      500:
        description: Internal server error
    """
    try:
        skip = int(request.args.get('skip', 0))
        limit = int(request.args.get('limit', 10))
        products = ProductRepository.get_products(skip, limit)
        return jsonify([product.to_dict() for product in products]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update an existing product by ID
@product_blueprint.route('/api/product/<int:product_id>/', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product by ID
    ---
    tags:
      - Product
    parameters:
      - name: product_id
        in: path
        type: integer
        required: True
      - name: body
        in: body
        required: True
        schema:
          type: object
          properties:
            name:
              type: string
            description:
              type: string
            price:
              type: number
            quantity:
              type: integer
    responses:
      200:
        description: Product updated successfully
      404:
        description: Product not found
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        quantity = data.get('quantity')
        updated_product = ProductRepository.update_product(product_id, name, description, price, quantity)
        if updated_product:
            return jsonify(updated_product.to_dict()), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a product by ID
@product_blueprint.route('/api/product/<int:product_id>/', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product by ID
    ---
    tags:
      - Product
    parameters:
      - name: product_id
        in: path
        type: integer
        required: True
    responses:
      204:
        description: Product deleted successfully
      404:
        description: Product not found
      500:
        description: Internal server error
    """
    try:
        deleted_product = ProductRepository.delete_product(product_id)
        if deleted_product:
            return jsonify(""), 204
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
