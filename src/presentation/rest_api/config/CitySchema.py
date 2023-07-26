#from src.presentation.rest_api.create_app import create_app
from src.infrastructure.persistence.cities.CityDBModelConfig import CityDBModelConfig


from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class CitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CityDBModelConfig
        load_instance = True
        include_fk = True
        include_relationship = True

