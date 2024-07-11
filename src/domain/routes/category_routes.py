from flask import Blueprint, request, jsonify
from src.application.repositories.category_repository import CategoryRepository

category_blueprint = Blueprint('category_bp', __name__)

# Create a new category
@category_blueprint.route('/api/category/', methods=['POST'])
def create_category():
    """
    Create a new category
    ---
    tags:
      - Category
    parameters:
      - name: body
        in: body
        required: True
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      201:
        description: Category created successfully
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        name = data.get('name')
        new_category = CategoryRepository.create_category(name)
        return jsonify(new_category.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a specific category by ID
@category_blueprint.route('/api/category/<int:category_id>/', methods=['GET'])
def get_category(category_id):
    """
    Get a specific category by ID
    ---
    tags:
      - Category
    parameters:
      - name: category_id
        in: path
        type: integer
        required: True
    responses:
      200:
        description: Category retrieved successfully
      404:
        description: Category not found
      500:
        description: Internal server error
    """
    try:
        category = CategoryRepository.get_category(category_id)
        if category:
            return jsonify(category.to_dict()), 200
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a list of categories with pagination
@category_blueprint.route('/api/category/', methods=['GET'])
def get_categories():
    """
    Get a list of categories with pagination
    ---
    tags:
      - Category
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
        description: Categories retrieved successfully
      500:
        description: Internal server error
    """
    try:
        skip = int(request.args.get('skip', 0))
        limit = int(request.args.get('limit', 10))
        categories = CategoryRepository.get_categories(skip, limit)
        return jsonify([category.to_dict() for category in categories]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update an existing category by ID
@category_blueprint.route('/api/category/<int:category_id>/', methods=['PUT'])
def update_category(category_id):
    """
    Update an existing category by ID
    ---
    tags:
      - Category
    parameters:
      - name: category_id
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
    responses:
      200:
        description: Category updated successfully
      404:
        description: Category not found
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        name = data.get('name')
        updated_category = CategoryRepository.update_category(category_id, name)
        if updated_category:
            return jsonify(updated_category.to_dict()), 200
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a category by ID
@category_blueprint.route('/api/category/<int:category_id>/', methods=['DELETE'])
def delete_category(category_id):
    """
    Delete a category by ID
    ---
    tags:
      - Category
    parameters:
      - name: category_id
        in: path
        type: integer
        required: True
    responses:
      204:
        description: Category deleted successfully
      404:
        description: Category not found
      500:
        description: Internal server error
    """
    try:
        deleted_category = CategoryRepository.delete_category(category_id)
        if deleted_category:
            return jsonify(""), 204
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
