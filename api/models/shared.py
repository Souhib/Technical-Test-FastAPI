from pydantic import ConfigDict
from sqlmodel import SQLModel


class DBModel(SQLModel):
    """
    Base model for database interactions.

    Attributes:
        model_config (ConfigDict): Configuration for the model, set to forbid extra fields and validate assignments.
    """

    model_config = ConfigDict(extra="forbid", validate_assignment=True)  # type: ignore
