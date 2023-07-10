from abc import ABC, abstractmethod


class CityRepository(ABC):
    """
        This class is the interface for CityRepository
    """

    @abstractmethod
    def get(self, city_id):
        pass

    @abstractmethod
    def save(self, city: str, province_id: str):
        pass


