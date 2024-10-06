from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Represents the application settings.

    Attributes:
        model_config (SettingsConfigDict): Configuration for the model, set to use the .env file for environment variables.
        database_url (str): The URL of the database to connect to.
    """
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    database_url: str
