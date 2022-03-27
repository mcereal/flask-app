from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ

DB_CONNECTION = environ.get('DB_CONNECTION')
print(DB_CONNECTION)

engine = create_engine(
    DB_CONNECTION)
if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import src.models.models
    Base.metadata.create_all(bind=engine)
