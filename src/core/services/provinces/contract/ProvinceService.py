from abc import ABC, abstractmethod


class ProvinceService(ABC):
    """
        This class is the interface for ProvinceService
    """

    @abstractmethod
    def add(self, province: str):
        pass

    @abstractmethod
    def get(self, province_id: int):
        pass


