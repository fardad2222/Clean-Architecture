from sqlalchemy import engine_from_config

from src.infrastructure.persistence import initialize_sql
from sqlalchemy import create_engine

from src.presentation.rest_api.config.BaseConfig import BaseConfig as app_config

engine = create_engine(app_config.DB_URI, echo=True)
initialize_sql(engine)

