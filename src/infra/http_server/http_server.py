from flask import Flask
from src.domain.routes.product_routes import product_blueprint
from src.infra.api_docs.api_docs_port import APIDocsPort

class HttpServer:
    def __init__(self, api_docs_port: APIDocsPort):
        self.api_docs_port = api_docs_port

    def run(self):
        app = Flask(__name__)
        app.register_blueprint(product_blueprint)
        app.config['JSON_SORT_KEYS'] = False

        # Configuração da documentação da API via porta
        self.api_docs_port.setup(app)

        app.run(host='0.0.0.0', debug=True)

