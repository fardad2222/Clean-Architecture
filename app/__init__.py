from sqlalchemy import engine_from_config

from app.infrastructure.persistence import initialize_sql
from sqlalchemy import create_engine

from BaseConfig import BaseConfig as app_config

engine = create_engine(app_config.DB_URI, echo=True)
initialize_sql(engine)

# def main(global_config, **settings):
#     """ This function returns a Pyramid WSGI application.
#     """
#     config = Configurator(settings=settings)
#     config.scan('app.infrastructure.persistence') # the "important" line
#     engine = engine_from_config(settings, 'sqlalchemy.')
#     initialize_sql(engine)
#     # other statements here
#     config.add_handler('main', '/{action}',
#                      'app.handlers:MyHandler')
#     return config.make_wsgi_app()