from flask import Flask

from .main.routes import main

def create_app():
    app = Flask(__name__)
    app.debug = True

    app.register_blueprint(main)
    
    return app