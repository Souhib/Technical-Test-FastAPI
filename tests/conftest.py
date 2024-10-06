import os

import pytest
from fastapi import FastAPI
from sqlalchemy import Engine, create_engine
from sqlmodel import Session, SQLModel

from api.controllers.frame import FrameController


@pytest.fixture(name="engine", scope="session", autouse=True)
def generate_socket_test_pgsql_engine():
    engine = create_engine("sqlite://")
    SQLModel.metadata.create_all(engine)
    yield engine


@pytest.fixture(name="session")
def generate_test_db_session(engine: Engine):
    with Session(engine) as session:
        yield session


@pytest.fixture(name="frame_controller")
def get_frame_controller(session: Session) -> FrameController:
    return FrameController(session)
