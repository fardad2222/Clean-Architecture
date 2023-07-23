# app/extensions
from src.presentation.rest_api.cities.CityAPI import city_api
from src.presentation.rest_api.provinces.ProvinceAPI import province_api



def register_routes(app):
    """ Register routes with blueprint and namespace """
    app.register_blueprint(city_api, url_prefix='/api/v1/')
    app.register_blueprint(province_api, url_prefix='/api/v1/')
