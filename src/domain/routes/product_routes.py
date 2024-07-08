from flask import Blueprint
product_blueprint = Blueprint('product_bp',__name__)

@product_blueprint.route('/product',methods=['POST'])
def create_poduct():
    return 'create_poduct'

@product_blueprint.route('/product',methods=['GET'])
def list_poducts():
    return 'list_poducts'

