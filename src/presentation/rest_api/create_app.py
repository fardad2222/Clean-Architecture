# ROOT_Project
from flask import Flask
from src.presentation.rest_api.config.BaseConfig import BaseConfig
from src.presentation.rest_api.config.RoutesExtension import register_routes
from src.presentation.rest_api.config.ExceptionExtension import register_exception_handler
# from src.presentation.rest_api.cities.CityAPI import CityJSONEncoder


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    # app.json_encoder = CityJSONEncoder
    register_routes(app)
    register_exception_handler(app)

    return app
