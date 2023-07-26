
from typing import Optional
import uuid
from sqlalchemy.exc import IntegrityError
from sqlalchemy import literal
from src.core.services.cities.contract.CityRepository import CityRepository
from src.core.entities.City import City
from src.infrastructure.persistence import DBSession
from src.infrastructure.persistence.cities.CityDBModelConfig import CityDBModelConfig
from src.presentation.rest_api.config.ErrorClasses import UniqueViolationError


class MySQLCityRepository(CityRepository):
    """ MySQL Repository for City
    """
    def __init__(self, session: DBSession):
        self.__session = session

    def __db_to_entity(
            self, db_row: CityDBModelConfig
    ) -> Optional[City]:
        return City(
            city_id=db_row.city_id,
            name=db_row.name,
            province_id=db_row.province_id
        )
    
    def exits_name(self, city, province_id):
        result = self.__session.query(CityDBModelConfig).filter(CityDBModelConfig.name == city, CityDBModelConfig.province_id == province_id).first()
        # result = self.__session.query(literal(True)).filter(result).scalar()
        if result is None:
            return False
        else: return True

    def save(self, name: str, province_id: int) -> Optional[CityDBModelConfig]:
        """ Create City
        :param name: str
        :return: Optional[City]
        """
        city_db_model = CityDBModelConfig(
            name=name,
            province_id=province_id
        )

        if city_db_model is not None:
            return city_db_model
        return None

    def get(self, city_id) -> Optional[CityDBModelConfig]:
        """ Get City by id
        :param city_id: CityId
        :return: Optional[City]
        """
        # result = self.__session.query(CityDBModelConfig).get(city_id)
        result = self.__session.query(CityDBModelConfig).filter(CityDBModelConfig.city_id == city_id)
        if result is not None:
            return result.first()
        return None
