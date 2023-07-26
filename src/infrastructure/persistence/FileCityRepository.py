import copy
import uuid
from typing import Dict
from src.core.value_objects import CityProvinceId
from src.core.services.cities.contract.CityRepository import CityRepository
from src.core.entities.City import City


class FileCityRepository(CityRepository):
    def __init__(self):
        self._city_province_list: Dict[CityProvinceId, City] = {}

    def get(self, city_id: CityProvinceId):
        return copy.deepcopy(self._city_province_list[CityProvinceId])
    
    def save(self, name: str, province_id: int):
        city_province = City(
            city_id=uuid.uuid4(),
            name=name,
            province_id=province_id
        )
        self._city_province_list[city_province.city_id] = city_province
        return self._city_province_list[city_province.city_id].city_id
