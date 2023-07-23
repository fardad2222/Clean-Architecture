from typing import Optional
import uuid
from sqlalchemy.exc import IntegrityError
from app.core.services.cities.contract.CityRepository import CityRepository
from app.core.entities.City import City
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.cities.CityDBModelConfig import CityDBModelConfig
from app.presentation.rest_api.config.ErrorClasses import UniqueViolationError


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

    def save(self, name: str, province_id: int) -> Optional[CityDBModelConfig]:
        """ Create City
        :param name: str
        :return: Optional[City]
        """
        city_db_model = CityDBModelConfig(
            name=name,
            province_id=province_id
        )

        try:
            # self.__session.add(city_db_model)
            # self.__session.flush()
            # self.__session.refresh(city_db_model)
            # return city_db_model.city_id

            self.__session.add(city_db_model)
            self.__session.commit()
            self.__session.refresh(city_db_model)
        except IntegrityError as exception:
            if "violates unique constraint" in str(exception.orig):
                raise UniqueViolationError(
                    "Profession with the same name already exists"
                ) from exception
            raise

        if city_db_model is not None:
            return self.__db_to_entity(city_db_model)
        return None

    def get(self, city_id) -> Optional[CityDBModelConfig]:
        """ Get City by id
        :param city_id: CityId
        :return: Optional[City]
        """
        result = self.__session.query(CityDBModelConfig).get(city_id)
        if result is not None:
            return self.__db_to_entity(result)
        return None
