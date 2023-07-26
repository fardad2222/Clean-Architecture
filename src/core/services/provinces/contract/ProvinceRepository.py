from abc import ABC, abstractmethod


class ProvinceRepository(ABC):
    """
        This class is the interface for ProvinceRepository
    """

    @abstractmethod
    def get(self, province_id):
        pass

    @abstractmethod
    def save(self, province: str):
        pass


