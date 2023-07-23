
import jsonpickle

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from app.core.services.cities.CityAppService import CityAPPService
from app.core.services.provinces.ProvinceAppService import ProvinceAPPService
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.UnitOfWork import UnitOfWork
from app.infrastructure.persistence.cities.MySQLCityRepository import MySQLCityRepository
from app.infrastructure.persistence.provinces.MySQLProvinceRepository import MySQLProvinceRepository


class AddCityAPI(Resource):
    def post(self):

        # city = request.form['city']
        # province = request.form['province_id']

        request_data = request.get_json()
        city = request_data['city']
        province = request_data['province_id']
       
        city_repository = MySQLCityRepository(DBSession)
        city_service = CityAPPService(city_repository)
        city_province_id = city_service.add(city, province)
     
        return jsonify({'city_id': str(city_province_id.city_id), 'city': str(city_province_id.name)})


class CityAPI(Resource):
    def get(self):
        city_province_id = request.args.get('id')

        city_province = CityAPPService(MySQLCityRepository())
        return city_province.get(city_province_id)

    def delete(self):
        city_province_id = request.args.get('id')

        city_province = CityAPPService(MySQLCityRepository())
        return city_province.delete(city_province_id)


city_api = Blueprint('rest_api/cities/name', __name__)
api = Api(city_api)
api.add_resource(AddCityAPI, '/cities', endpoint='cities')
api.add_resource(CityAPI, '/cities/<int:id>', endpoint='name')


