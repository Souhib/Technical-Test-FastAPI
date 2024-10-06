from functools import lru_cache

from fastapi import Depends
from sqlalchemy import Engine
from sqlmodel import Session

from api.controllers.frame import FrameController
from api.database import create_app_engine
from api.settings import Settings


@lru_cache()
def get_settings():
    """
    Function to get the application settings.

    Returns:
        Settings: The application settings.
    """
    return Settings()


async def get_engine():
    """
    Function to get the application engine.

    Returns:
        Engine: The application engine.
    """
    return create_app_engine()


async def get_session(engine: Engine = Depends(get_engine)):
    """
    Function to get the application session.

    Args:
        engine (Engine): The application engine.

    Returns:
        Session: The application session.
    """
    with Session(engine) as session:
        yield session


async def get_frame_controller(
    session: Session = Depends(get_session),
) -> FrameController:
    """
    Function to get the frame controller.

    Args:
        session (Session): The application session.

    Returns:
        FrameController: The frame controller.
    """
    return FrameController(session)