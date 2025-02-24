from flask import Flask 
from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    """"Application factory function."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inizialise Flask-RESTx
    from app.presentation.api  import api
    api.init_app(app)

    return app