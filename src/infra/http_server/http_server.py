from flask import Flask
from src.domain.routes.product_routes import product_blueprint
from src.infra.api_docs.api_docs_port import APIDocsPort

class HttpServer:
    def __init__(self, api_docs_port: APIDocsPort):
        self.api_docs_port = api_docs_port
        self.app = Flask(__name__)
        self.app.register_blueprint(product_blueprint)
        self.app.config['JSON_SORT_KEYS'] = False
        self.api_docs_port.setup(self.app)
        
    def run(self):
        self.app.run(host='0.0.0.0', debug=True)
