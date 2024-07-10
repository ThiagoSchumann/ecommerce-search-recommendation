from flask import jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from src.infra.api_docs.api_docs_port import APIDocsPort

class SwaggerAdapter(APIDocsPort):
    def setup(self, app):
        @app.route('/api/docs/')
        def docs():
            swag = swagger(app)
            swag['info']['title'] = "ecommerce-search-recommendation"
            swag['info']['description'] = "API for managing products"
            swag['info']['version'] = "1.0"
            return jsonify(swag)

        # Configuração do Swagger UI
        SWAGGER_URL = '/api/docs/swagger'
        API_URL = '/api/docs/'
        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={
                'app_name': "ecommerce-search-recommendation"
            }
        )
        app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
