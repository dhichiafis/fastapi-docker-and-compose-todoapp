from pydantic_settings import BaseSettings,SettingsConfigDict

class Setting(BaseSettings):
    DB_URL:str 

    model_config=SettingsConfigDict(env_file=".env")

settings=Setting()