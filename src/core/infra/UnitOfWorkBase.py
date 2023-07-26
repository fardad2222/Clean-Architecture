
from abc import ABC, abstractmethod

class UnitOfWorkBase(ABC):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback()

