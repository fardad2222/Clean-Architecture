
from src.core.services.cities.contract import CityService
from src.core.services.cities.contract.CityRepository import CityRepository
from src.infrastructure.persistence import DBSession
from src.infrastructure.persistence.UnitOfWork import UnitOfWork


class CityAPPService(CityService.CityService):
    """
        This class is responsible for creating a new City
    """

    def __init__(self, repository: CityRepository, unitOfWork: UnitOfWork):
        self.repository = repository
        self.unitOfWork = unitOfWork

    def add(self, city, province_id):
        with self.unitOfWork as uow:
            if self.repository.exits_name(city, province_id) is False:
                city_model = self.repository.save(city, province_id)
                uow.session.add(city_model)
                uow.session.commit()
                uow.session.refresh(city_model)
                id = city_model.city_id
                uow.session.close()
                return id
            else:
                raise Exception("City %s already exists" % city)

    def get(self, city_id):
        return self.repository.get(city_id)
