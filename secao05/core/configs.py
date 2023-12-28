from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:123@localhost:5432/Faculdade'
    
    class Config:
        case_sensitive = True
        
settings = Settings()