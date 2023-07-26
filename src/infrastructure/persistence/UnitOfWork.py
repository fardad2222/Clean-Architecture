
from contextlib import contextmanager
from src.core.infra.UnitOfWorkBase import UnitOfWorkBase
from src.core.services.cities import CityAppService
from src.core.services.cities.contract import CityRepository
from src.core.services.provinces.contract import ProvinceRepository
from src.infrastructure.persistence import DBSession

# Define the unit of work class
class UnitOfWork(UnitOfWorkBase):
    def __init__(self, session: DBSession) -> None:
        self.session = session
    
    def __enter__(self):
        self.session = DBSession()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

    @contextmanager
    def get_session(self):
        """Helper function to manage sessions"""
        session = DBSession()
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()

