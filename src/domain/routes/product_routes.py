from flask import Blueprint,request,jsonify
from src.application.repositories.product_repository import ProductRepository

product_blueprint = Blueprint('product_bp',__name__)

@product_blueprint.route('/product',methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        name = data.get('name')
        new_product = ProductRepository.create_product(name)
        return jsonify({"message": "Product created", "product": repr(new_product)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@product_blueprint.route('/product',methods=['GET'])
def list_poducts():
    return 'list_poducts'

