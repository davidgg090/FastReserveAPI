from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
        Settings class for managing configuration settings

        Args:
            database_url (str): The URL of the database.

        Config:
            env_file (str): The path to the environment file.
    """

    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
