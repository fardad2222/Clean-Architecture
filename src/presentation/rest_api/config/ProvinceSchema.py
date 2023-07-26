
from src.infrastructure.persistence.provinces.ProvinceDBModelConfig import ProvinceDBModelConfig
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class ProvinceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProvinceDBModelConfig
        include_fk = False
        load_instance = True
        include_relationships = True

