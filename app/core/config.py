from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
        Settings class for managing configuration settings

        Args:
            database_url (str): The URL of the database.
            secret_key (str): The secret key for the application.
            algorithm (str): The algorithm to use for the JWT.
            access_token_expire_minutes (int): The number of minutes before the access token expires.

        Config:
            env_file (str): The path to the environment file.
    """

    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
