from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from api.settings import Settings


def create_app_engine() -> Engine:
    """
    Creates and returns a SQLAlchemy engine instance for the application.

    This function initializes a SQLAlchemy engine using the database URL from the application settings.
    It sets the 'check_same_thread' argument to False to allow connections to be shared across threads,
    and enables SQL statement echoing for debugging purposes.

    Returns:
        Engine: The created SQLAlchemy engine instance.
    """
    settings = Settings()
    print("DATABASE URL : ", settings.database_url)
    engine = create_engine(
        settings.database_url, connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {}, echo=True
    )
    return engine


def create_db_and_tables(engine: Engine):
    """
    Creates all database tables based on SQLModel metadata using the provided engine.

    This function uses the SQLModel metadata to create all database tables associated with the models defined
    within the application. It is intended to be called once during application initialization to set up the
    database schema.

    Args:
        engine (Engine): The SQLAlchemy engine instance to use for creating the database tables.
    """
    SQLModel.metadata.create_all(engine)
