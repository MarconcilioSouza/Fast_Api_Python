from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:123@localhost:5432/Faculdade"
    DBBaseModel = declarative_base()
    
    JWT_SECRET: str = 'LKAn6FJuyz0t9ht_Y00Dbunj9UfmHGM'
    """ Obter o token via python
        import secrets
        token: str = secrets.token_urlsafe(23)
    """
    ALGORITHM: str = 'HS256'
    
    ACCESS_TOKEN_EXPRIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive= True
        
settings = Settings()
