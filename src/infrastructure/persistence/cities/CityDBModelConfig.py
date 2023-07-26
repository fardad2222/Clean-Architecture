"""
    Entity CityProvince data Model 
"""

from datetime import date

from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from src.infrastructure.persistence import Base
from src.infrastructure.persistence.provinces.ProvinceDBModelConfig import ProvinceDBModelConfig


class CityDBModelConfig(Base):
    """
        Defines the City database model.
    """
    
    __tablename__ = 'cities'
    
    city_id : Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement=True, nullable = False, unique = True)
    name : Mapped[str] = mapped_column(String(80), nullable = False, unique = False)
    province_id : Mapped[int] = mapped_column(Integer, ForeignKey('provinces.province_id'), nullable = False)
    province : Mapped["ProvinceDBModelConfig"] = relationship(back_populates= 'cities')
    

