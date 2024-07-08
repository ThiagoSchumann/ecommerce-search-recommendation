from flask import Flask
from src.domain.routes.product_routes import product_blueprint



class HttpServer:
    def run(self):
        app = Flask(__name__)
        app.register_blueprint(product_blueprint)
        app.config['JSON_SORT_KEYS'] = False
        app.run(host='0.0.0.0',debug=True,)
