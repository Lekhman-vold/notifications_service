from functools import lru_cache
from pydantic import BaseSettings
from pydantic.fields import Field


class SMTP(BaseSettings):
	server: str = Field(env='SMTP_SERVER')
	port: int = Field(env='SMTP_PORT')
	username: str = Field(env='SMTP_USERNAME')
	password: str = Field(env='SMTP_PASSWORD')

	class Config:
		env_file = '.env'
		env_file_encoding = 'utf-8'


class Settings(BaseSettings):
	host: str = Field(env='HOST', default='0.0.0.0')
	port: int = Field(env='PORT', default=8080)

	smtp: SMTP = SMTP()

	class Config:
		env_file = '.env'
		env_file_encoding = 'utf-8'


@lru_cache()
def get_settings() -> Settings:
	return Settings()
