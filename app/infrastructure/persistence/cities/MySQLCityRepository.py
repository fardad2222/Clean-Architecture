from typing import Optional
import uuid
from sqlalchemy.exc import IntegrityError
from app.core.services.cities.contract.CityRepository import CityRepository
# from app.core.entities.City import City
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.cities.CityDBModelConfig import CityDBModelConfig
from app.presentation.rest_api.config.ErrorClasses import UniqueViolationError
from app.infrastructure.persistence.UnitOfWork import UnitOfWork


class MySQLCityRepository(CityRepository):
    """ MySQL Repository for City
    """
    def __init__(self) -> None:
        self.__session = DBSession

    def __db_to_entity(
            self, db_row: CityDBModelConfig
    ) -> Optional[CityDBModelConfig]:
        return CityDBModelConfig(
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
            with UnitOfWork as uow:
                with uow.get_session() as session:
                    session.add(city_db_model)
                    session.commit()
                    session.refresh(city_db_model)
        except IntegrityError as exception:
            if "violates unique constraint" in str(exception.orig):
                raise UniqueViolationError(
                    "Profession with the same name already exists"
                ) from exception
            raise

        if city_db_model is not None:
            return self.__db_to_entity(city_db_model)
        return None

    def get(self, city_id: CityDBModelConfig.city_id) -> Optional[CityDBModelConfig]:
        """ Get City by id
        :param city_id: CityId
        :return: Optional[City]
        """
        result = self.__session.query(CityDBModelConfig).get(city_id)
        if result is not None:
            return self.__db_to_entity(result)
        return None
