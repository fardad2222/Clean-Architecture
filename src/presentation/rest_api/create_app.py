# ROOT_Project
from flask import Flask
from src.presentation.rest_api.config.BaseConfig import BaseConfig
from src.presentation.rest_api.config.RoutesExtension import register_routes
from src.presentation.rest_api.config.ExceptionExtension import register_exception_handler


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    register_routes(app)
    register_exception_handler(app)

    return app
