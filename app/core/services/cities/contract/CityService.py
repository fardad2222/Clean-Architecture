from abc import ABC, abstractmethod


class CityService(ABC):
    """
        This class is the interface for CityService
    """

    @abstractmethod
    def add(self, city: str, province_id: str):
        pass

    @abstractmethod
    def get(self, city_id: str):
        pass


